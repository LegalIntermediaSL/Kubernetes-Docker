#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


ROOT = Path("examples/k8s")

BASE_NAMESPACES = {
    Path("hola-nginx"): "hola-nginx-demo",
    Path("python-api"): "python-api-demo",
    Path("configmap-secret"): "config-demo",
    Path("ingress-demo"): "ingress-demo",
    Path("job-cronjob"): "batch-demo",
}

BUILTIN_API_VERSIONS = {
    "v1",
    "apps/v1",
    "batch/v1",
    "networking.k8s.io/v1",
    "autoscaling/v2",
    "policy/v1",
    "rbac.authorization.k8s.io/v1",
    "scheduling.k8s.io/v1",
}


def fail(path: Path, message: str) -> None:
    raise AssertionError(f"{path}: {message}")


def ensure(condition: bool, path: Path, message: str) -> None:
    if not condition:
        fail(path, message)


def ensure_containers(doc: dict[str, Any], path: Path, location: list[str]) -> None:
    cursor: Any = doc
    for key in location:
        cursor = cursor.get(key) if isinstance(cursor, dict) else None
    ensure(isinstance(cursor, list) and cursor, path, "must declare at least one container")


def validate_builtin(doc: dict[str, Any], path: Path) -> None:
    kind = doc["kind"]
    metadata = doc.get("metadata") or {}
    spec = doc.get("spec") or {}

    if kind == "Namespace":
        return

    if kind == "ConfigMap":
        ensure(doc.get("data") or doc.get("binaryData"), path, "ConfigMap should include data or binaryData")
        return

    if kind == "Secret":
        ensure(doc.get("data") or doc.get("stringData"), path, "Secret should include data or stringData")
        ensure(metadata.get("name"), path, "Secret must have metadata.name")
        return

    if kind == "PriorityClass":
        ensure(doc.get("value") is not None, path, "PriorityClass must declare value")
        return

    if kind == "ServiceAccount":
        return

    if kind == "Role":
        ensure(doc.get("rules"), path, "Role must declare rules")
        return

    if kind == "RoleBinding":
        ensure(doc.get("roleRef"), path, "RoleBinding must declare roleRef")
        ensure(doc.get("subjects"), path, "RoleBinding must declare subjects")
        return

    ensure(spec, path, f"{kind} missing spec")

    if kind == "Deployment":
        selector = spec.get("selector", {}).get("matchLabels")
        labels = spec.get("template", {}).get("metadata", {}).get("labels")
        ensure(selector, path, "Deployment must declare spec.selector.matchLabels")
        ensure(labels, path, "Deployment must declare template labels")
        ensure_containers(doc, path, ["spec", "template", "spec", "containers"])
        return

    if kind == "Service":
        ports = spec.get("ports")
        ensure(isinstance(ports, list) and ports, path, "Service must declare ports")
        if spec.get("type") != "ExternalName":
            ensure(spec.get("selector"), path, "Service should declare a selector unless it is ExternalName")
        return

    if kind == "Ingress":
        ensure(spec.get("rules") or spec.get("defaultBackend"), path, "Ingress must declare rules or defaultBackend")
        return

    if kind == "PodDisruptionBudget":
        ensure(spec.get("selector"), path, "PodDisruptionBudget must declare selector")
        ensure(
            spec.get("minAvailable") is not None or spec.get("maxUnavailable") is not None,
            path,
            "PodDisruptionBudget must declare minAvailable or maxUnavailable",
        )
        return

    if kind == "Job":
        ensure_containers(doc, path, ["spec", "template", "spec", "containers"])
        ensure(spec.get("template", {}).get("spec", {}).get("restartPolicy"), path, "Job must set restartPolicy")
        return

    if kind == "CronJob":
        ensure(spec.get("schedule"), path, "CronJob must declare schedule")
        template_spec = spec.get("jobTemplate", {}).get("spec", {}).get("template", {}).get("spec", {})
        ensure(isinstance(template_spec.get("containers"), list) and template_spec.get("containers"), path, "CronJob must declare containers")
        ensure(template_spec.get("restartPolicy"), path, "CronJob must set restartPolicy")
        return

    if kind == "PersistentVolumeClaim":
        ensure(spec.get("accessModes"), path, "PersistentVolumeClaim must declare accessModes")
        storage = ((spec.get("resources") or {}).get("requests") or {}).get("storage")
        ensure(storage, path, "PersistentVolumeClaim must request storage")
        return

    if kind == "LimitRange":
        ensure(spec.get("limits"), path, "LimitRange must declare spec.limits")
        return

    if kind == "ResourceQuota":
        ensure(spec.get("hard"), path, "ResourceQuota must declare spec.hard")
        return

    if kind == "PersistentVolume":
        capacity = (spec.get("capacity") or {}).get("storage")
        ensure(capacity, path, "PersistentVolume must declare capacity.storage")
        ensure(spec.get("accessModes"), path, "PersistentVolume must declare accessModes")
        return

    if kind == "NetworkPolicy":
        ensure(spec.get("podSelector") is not None, path, "NetworkPolicy must declare podSelector")
        ensure(spec.get("policyTypes") or spec.get("ingress") or spec.get("egress"), path, "NetworkPolicy should declare policyTypes, ingress or egress")
        return

    if kind == "StatefulSet":
        ensure(spec.get("serviceName"), path, "StatefulSet must declare serviceName")
        ensure(spec.get("selector"), path, "StatefulSet must declare selector")
        ensure_containers(doc, path, ["spec", "template", "spec", "containers"])
        return

    if kind == "HorizontalPodAutoscaler":
        ensure(spec.get("scaleTargetRef"), path, "HorizontalPodAutoscaler must declare scaleTargetRef")
        ensure(spec.get("maxReplicas"), path, "HorizontalPodAutoscaler must declare maxReplicas")
        ensure(spec.get("metrics"), path, "HorizontalPodAutoscaler should declare metrics")
        return

    if kind == "Pod":
        ensure_containers(doc, path, ["spec", "containers"])
        return

def validate_base_namespace(path: Path, doc: dict[str, Any]) -> None:
    relative = path.relative_to(ROOT)
    example_dir = Path(relative.parts[0])
    expected = BASE_NAMESPACES.get(example_dir)
    if not expected or doc.get("kind") == "Namespace":
        return

    namespace = (doc.get("metadata") or {}).get("namespace")
    ensure(namespace == expected, path, f"expected metadata.namespace={expected!r}")


def main() -> None:
    namespace_files = {example_dir / "namespace.yaml" for example_dir in BASE_NAMESPACES}

    for namespace_file in namespace_files:
        ensure((ROOT / namespace_file).exists(), ROOT / namespace_file, "missing namespace manifest")

    for path in sorted(ROOT.rglob("*.yaml")):
        if "templates" in path.parts:
            continue
        if "kustomize-demo" in path.parts:
            continue
        if path.name == "Chart.yaml" or "values" in path.stem:
            continue

        docs = list(yaml.safe_load_all(path.read_text()))
        for doc in docs:
            if doc is None:
                continue

            ensure(isinstance(doc, dict), path, "document must be a mapping")
            ensure(doc.get("apiVersion"), path, "missing apiVersion")
            ensure(doc.get("kind"), path, "missing kind")
            if doc.get("kind") == "Kustomization":
                continue

            metadata = doc.get("metadata") or {}
            ensure(metadata.get("name"), path, "missing metadata.name")
            validate_base_namespace(path, doc)

            if doc["apiVersion"] in BUILTIN_API_VERSIONS:
                validate_builtin(doc, path)

    print("OK: offline Kubernetes semantic checks")


if __name__ == "__main__":
    main()

SHELL := /bin/bash
.DEFAULT_GOAL := help

KIND_CLUSTER ?= curso-k8s-ci
MINIKUBE_PROFILE ?= curso-k8s-ci
PYTHON_API_IMAGE ?= python-api:local
PYTHON_API_DEMO_IMAGE ?= ghcr.io/example/kubernetes-docker-python-api:1.0.0

.PHONY: help check-prereqs kind-up kind-load-python-api minikube-up minikube-enable-ingress minikube-load-python-api minikube-load-python-api-demo-tag build-python-api deploy-kustomize-dev verify-kustomize-dev deploy-helm-dev verify-helm-dev install-cert-manager deploy-cert-manager-demo verify-cert-manager-demo install-argocd deploy-argocd-demo-apps-local deploy-argocd-demo-root install-observability deploy-observability-demo verify-grafana status

help:
	@echo "Objetivos disponibles:"
	@echo "  make check-prereqs                 Verifica herramientas locales"
	@echo "  make kind-up                       Crea un cluster kind si no existe"
	@echo "  make kind-load-python-api          Carga python-api:local en kind"
	@echo "  make minikube-up                   Levanta minikube con Docker"
	@echo "  make minikube-enable-ingress       Activa el addon ingress en minikube"
	@echo "  make build-python-api              Construye la imagen python-api:local"
	@echo "  make minikube-load-python-api      Carga python-api:local en minikube"
	@echo "  make minikube-load-python-api-demo-tag"
	@echo "                                     Carga tambien la etiqueta usada por el overlay demo"
	@echo "  make deploy-kustomize-dev          Despliega el overlay dev de Kustomize"
	@echo "  make verify-kustomize-dev          Verifica /health y /metrics del despliegue Kustomize"
	@echo "  make deploy-helm-dev               Instala el chart Helm en helm-demo"
	@echo "  make verify-helm-dev               Verifica /health y /metrics del despliegue Helm"
	@echo "  make install-cert-manager          Instala cert-manager con Helm"
	@echo "  make deploy-cert-manager-demo      Aplica la demo self-signed"
	@echo "  make verify-cert-manager-demo      Comprueba el Certificate y el Secret TLS"
	@echo "  make install-argocd                Instala Argo CD con server-side apply"
	@echo "  make deploy-argocd-demo-apps-local Aplica AppProject y child apps locales"
	@echo "  make deploy-argocd-demo-root       Aplica AppProject y root app remota"
	@echo "  make install-observability         Instala kube-prometheus-stack"
	@echo "  make deploy-observability-demo     Aplica ServiceMonitor, PrometheusRule y dashboard"
	@echo "  make verify-grafana                Verifica Grafana por /login"
	@echo "  make status                        Resume el estado del laboratorio"

check-prereqs:
	@for bin in docker kubectl helm curl; do \
		command -v $$bin >/dev/null || { echo "Falta $$bin"; exit 1; }; \
	done
	@if ! command -v minikube >/dev/null && ! command -v kind >/dev/null; then \
		echo "Falta minikube o kind"; \
		exit 1; \
	fi

kind-up:
	@if command -v kind >/dev/null; then \
		if kind get clusters | grep -qx "$(KIND_CLUSTER)"; then \
			echo "kind $(KIND_CLUSTER) ya existe"; \
		else \
			kind create cluster --name "$(KIND_CLUSTER)"; \
		fi; \
	else \
		echo "kind no esta instalado"; \
		exit 1; \
	fi

kind-load-python-api:
	kind load docker-image "$(PYTHON_API_IMAGE)" --name "$(KIND_CLUSTER)"

minikube-up:
	minikube start --driver=docker --profile "$(MINIKUBE_PROFILE)"

minikube-enable-ingress:
	minikube addons enable ingress -p "$(MINIKUBE_PROFILE)"

build-python-api:
	docker build -t "$(PYTHON_API_IMAGE)" examples/docker/python-api

minikube-load-python-api:
	minikube image load "$(PYTHON_API_IMAGE)" -p "$(MINIKUBE_PROFILE)"

minikube-load-python-api-demo-tag:
	docker tag "$(PYTHON_API_IMAGE)" "$(PYTHON_API_DEMO_IMAGE)"
	minikube image load "$(PYTHON_API_DEMO_IMAGE)" -p "$(MINIKUBE_PROFILE)"

deploy-kustomize-dev:
	kubectl apply -k examples/k8s/kustomize-demo/overlays/dev
	kubectl -n kustomize-dev rollout status deployment/python-api --timeout=180s

verify-kustomize-dev:
	@kubectl -n kustomize-dev port-forward service/python-api 18080:80 >/tmp/pf-kustomize.log 2>&1 & \
	PF_PID=$$!; \
	trap 'kill $$PF_PID >/dev/null 2>&1 || true' EXIT; \
	sleep 5; \
	echo "HEALTH"; \
	curl -fsS http://127.0.0.1:18080/health; \
	echo; \
	echo "METRICS"; \
	curl -fsS http://127.0.0.1:18080/metrics | sed -n '1,10p'

deploy-helm-dev:
	helm upgrade --install python-api-demo examples/helm/python-api \
		-n helm-demo \
		--create-namespace \
		-f examples/helm/python-api/values-dev.yaml \
		--set image.tag=local
	kubectl -n helm-demo rollout status deployment/python-api-demo-python-api --timeout=180s

verify-helm-dev:
	@kubectl -n helm-demo port-forward service/python-api-demo-python-api 18081:80 >/tmp/pf-helm.log 2>&1 & \
	PF_PID=$$!; \
	trap 'kill $$PF_PID >/dev/null 2>&1 || true' EXIT; \
	sleep 5; \
	echo "HEALTH"; \
	curl -fsS http://127.0.0.1:18081/health; \
	echo; \
	echo "METRICS"; \
	curl -fsS http://127.0.0.1:18081/metrics | sed -n '1,10p'

install-cert-manager:
	helm repo add jetstack https://charts.jetstack.io
	helm repo update
	helm upgrade --install cert-manager jetstack/cert-manager \
		-n cert-manager \
		--create-namespace \
		--set crds.enabled=true
	kubectl -n cert-manager rollout status deployment/cert-manager --timeout=300s
	kubectl -n cert-manager rollout status deployment/cert-manager-webhook --timeout=300s
	kubectl -n cert-manager rollout status deployment/cert-manager-cainjector --timeout=300s

deploy-cert-manager-demo:
	kubectl apply -f examples/k8s/cert-manager-demo/namespace.yaml
	kubectl apply -f examples/k8s/cert-manager-demo/clusterissuer-selfsigned.yaml
	kubectl apply -f examples/k8s/cert-manager-demo/deployment.yaml
	kubectl apply -f examples/k8s/cert-manager-demo/service.yaml
	kubectl apply -f examples/k8s/cert-manager-demo/certificate.yaml
	kubectl -n cert-manager-demo wait --for=condition=Ready certificate/python-api-tls --timeout=300s

verify-cert-manager-demo:
	kubectl -n cert-manager-demo get certificate python-api-tls
	kubectl -n cert-manager-demo get secret python-api-tls

install-argocd:
	kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -
	kubectl apply --server-side -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
	kubectl -n argocd rollout status deployment/argocd-server --timeout=300s
	kubectl -n argocd rollout status deployment/argocd-repo-server --timeout=300s
	kubectl -n argocd rollout status statefulset/argocd-application-controller --timeout=300s

deploy-argocd-demo-apps-local:
	kubectl apply -n argocd -f examples/k8s/argocd-practical-demo/project.yaml
	kubectl apply -n argocd -f examples/k8s/argocd-practical-demo/applications/python-api-helm-demo.yaml
	kubectl apply -n argocd -f examples/k8s/argocd-practical-demo/applications/python-api-kustomize-demo.yaml
	kubectl -n argocd get applications

deploy-argocd-demo-root:
	kubectl apply -n argocd -f examples/k8s/argocd-practical-demo/project.yaml
	kubectl apply -n argocd -f examples/k8s/argocd-practical-demo/root-application.yaml
	kubectl -n argocd get applications

install-observability:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm repo update
	helm upgrade --install observability prometheus-community/kube-prometheus-stack \
		-n observability \
		--create-namespace \
		-f examples/k8s/observability-stack-demo/kube-prometheus-stack-values.yaml
	kubectl -n observability rollout status deployment/observability-kube-prometh-operator --timeout=300s
	kubectl -n observability rollout status deployment/observability-grafana --timeout=300s
	kubectl -n observability rollout status deployment/observability-kube-state-metrics --timeout=300s
	kubectl -n observability rollout status statefulset/prometheus-observability-kube-prometh-prometheus --timeout=300s

deploy-observability-demo:
	kubectl apply -n kustomize-dev -f examples/k8s/observability-stack-demo/python-api-service-monitor.yaml
	kubectl apply -n kustomize-dev -f examples/k8s/observability-stack-demo/python-api-prometheus-rule.yaml
	kubectl apply -n observability -f examples/k8s/observability-stack-demo/grafana-dashboard-python-api.yaml

verify-grafana:
	@kubectl -n observability port-forward service/observability-grafana 13000:80 >/tmp/pf-grafana.log 2>&1 & \
	PF_PID=$$!; \
	trap 'kill $$PF_PID >/dev/null 2>&1 || true' EXIT; \
	sleep 5; \
	curl -fsSI http://127.0.0.1:13000/login | sed -n '1,8p'

status:
	@echo "CONTEXT"; \
	kubectl config current-context || true; \
	echo; \
	echo "APPLICATIONS"; \
	kubectl -n argocd get applications 2>/dev/null || true; \
	echo; \
	echo "KUSTOMIZE-DEV"; \
	kubectl -n kustomize-dev get pods,svc 2>/dev/null || true; \
	echo; \
	echo "HELM-DEMO"; \
	kubectl -n helm-demo get pods,svc 2>/dev/null || true; \
	echo; \
	echo "CERT-MANAGER-DEMO"; \
	kubectl -n cert-manager-demo get certificate,secret 2>/dev/null || true; \
	echo; \
	echo "OBSERVABILITY"; \
	kubectl -n observability get pods 2>/dev/null || true

{{- define "fullstack-demo.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "fullstack-demo.fullname" -}}
{{- .Release.Name -}}
{{- end -}}

{{- define "fullstack-demo.labels" -}}
app.kubernetes.io/name: {{ include "fullstack-demo.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
{{- end -}}

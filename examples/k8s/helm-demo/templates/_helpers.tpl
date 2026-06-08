{{- define "python-api-demo.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "python-api-demo.fullname" -}}
{{- .Release.Name -}}
{{- end -}}

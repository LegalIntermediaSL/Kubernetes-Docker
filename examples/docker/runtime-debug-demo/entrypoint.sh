#!/bin/sh
set -eu

echo "runtime-debug-demo iniciado pid=$$ modo=${APP_MODE:-demo}"

trap 'echo "SIGTERM recibido, cerrando limpio"; exit 0' TERM
trap 'echo "SIGINT recibido, cerrando limpio"; exit 0' INT

while true; do
  echo "$(date '+%Y-%m-%dT%H:%M:%S%z') heartbeat modo=${APP_MODE:-demo}"
  sleep 5 &
  wait $!
done

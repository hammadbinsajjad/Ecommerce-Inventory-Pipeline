#!/bin/bash

# Load .env file
set -a
source .env
set +a

env_flags=()
while IFS='=' read -r key value; do
  [[ "$key" =~ ^#.*$ || -z "$key" ]] && continue
  env_flags+=("-e" "$key=${!key}")
done < .env

cd orchestration

docker build . -t ecom_inv_kestra

# If the image is built, run it
if [ $? -eq 0 ]; then
  docker run --rm -it \
    --name ecom_inv_kestra \
    -v $(pwd)/kestra_config.yml:/app/config/kestra_config.yml \
    -p 8080:8080 \
    "${env_flags[@]}" \
    ecom_inv_kestra
else
  echo "Docker image build failed. Exiting..."
  exit 1
fi

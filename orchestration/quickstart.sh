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

docker build . -t ecom_inv_kestra

# If the image is built, run it
if [ $? -eq 0 ]; then
  docker run --rm -it \
    --name ecom_inv_kestra \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp:/tmp \
    -p 8080:8080 \
    "${env_flags[@]}" \
    ecom_inv_kestra
else
  echo "Docker image build failed. Exiting..."
  exit 1
fi

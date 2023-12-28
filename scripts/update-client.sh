#!/usr/bin/env bash

set -euxo pipefail

cd "$(dirname "$0")/../src/exist_client"

mkdir -p exist_io_client

# https://github.com/openapi-generators/openapi-python-client
openapi-python-client update --path ../../openapi-schemas/exist.yaml --meta none

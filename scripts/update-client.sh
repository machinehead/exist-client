#!/usr/bin/env bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR/../src/exist_client"

mkdir -p _exist_io_client

# https://github.com/openapi-generators/openapi-python-client
openapi-python-client update --path ../../openapi-schemas/exist.yaml --meta none --config $SCRIPT_DIR/client-generator-config.yaml

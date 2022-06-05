#!/bin/bash

### Bash Options
set -o errexit
set -o nounset
set -o pipefail


### Configuration
PROJECT_NAME="fastmodel"


### Operations
uvicorn $PROJECT_NAME.http:router --reload

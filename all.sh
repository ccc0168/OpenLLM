#!/usr/bin/env bash

GIT_ROOT=$(git rev-parse --show-toplevel)
cd "$GIT_ROOT" || exit 1

printf "Running update-mypy.py\n"
python ./tools/update-mypy.py
printf "Running update-config-stubs.py\n"
python ./tools/dependencies.py
printf "Running dependencies.py\n"
python ./tools/update-config-stubs.py
printf "Running update-readme.py\n"
python ./tools/update-readme.py
printf "Running mirror.sh\n"
bash ./tools/mirror.sh

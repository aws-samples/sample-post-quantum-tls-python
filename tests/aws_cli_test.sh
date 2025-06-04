#!/usr/bin/env bash

set -e

aws --region us-east-2 secretsmanager list-secrets >/dev/null
echo "ok"

#! /bin/bash

set -e

echo -n "Crypto library: "
python3 tests/check_crypto_library.py
echo -n "Testing ssl socket... "
python3 tests/ssl_socket_test.py
echo -n "Testing requests... "
python3 tests/requests_test.py
echo -n "Testing boto3... "
python3 tests/boto_client_test.py
echo -n "Testing AWS CLI... "
bash tests/aws_cli_test.sh

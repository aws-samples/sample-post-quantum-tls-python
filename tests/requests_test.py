import os
import ssl

import requests

REGION = "us-east-1"
ENDPOINT = f"https://secretsmanager.{REGION}.amazonaws.com/ping"

response = requests.get(ENDPOINT, timeout=3)
assert response.status_code == 200
print("ok")

import ssl
import socket

CERT_STORE = "/etc/ssl/certs/ca-certificates.crt"
REGION = "us-west-1"
HOST = f"secretsmanager.{REGION}.amazonaws.com"


ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# NOTE: we set minimum version of TLSv1.3 to prevent the server from
# down-grading connection to (non-PQ) TLSv1.2 negotiated by ciphersuites
# rather than (≥ TLSv1.3) SupportedGroups.
ctx.minimum_version = ssl.TLSVersion.TLSv1_3
ctx.load_verify_locations(CERT_STORE)
sock = socket.create_connection((HOST, 443))
ssock = ctx.wrap_socket(sock, server_hostname=HOST)
ssock.close()
print("ok")

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
with socket.create_connection((HOST, 443)) as s:
    with ctx.wrap_socket(s, server_hostname=HOST) as ss:
        ss.send(f"GET /ping HTTP/1.1\r\nHost: {HOST}\r\n\r\n".encode())
        assert b"200 OK" in ss.recv(4096)
print("ok")

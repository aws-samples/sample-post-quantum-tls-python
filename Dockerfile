FROM debian:trixie-20250428

RUN apt-get update
RUN apt-get install -y \
    python3=3.13.3-1 \
    python3-venv=3.13.3-1 \
    openssl=3.5.0-1

COPY . /app
WORKDIR /app

RUN python3 -m venv /app/.venv \
    && . /app/.venv/bin/activate \
    && python3 -m pip install -r /app/requirements.txt

ENTRYPOINT ["/bin/bash", "--init-file", "/app/.venv/bin/activate", "-i"]

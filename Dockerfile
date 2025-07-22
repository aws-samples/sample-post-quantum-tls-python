FROM debian:trixie-20250428

# Restrict debian repositories to official trixie
RUN rm -f /etc/apt/sources.list.d/*
RUN cat <<EOF >/etc/apt/sources.list.d/sources.list
deb http://deb.debian.org/debian trixie main
deb http://deb.debian.org/debian trixie-updates main
deb http://deb.debian.org/debian-security trixie-security main
EOF
RUN apt-get update
RUN apt-get install -y \
    python3>=3.13.3-1 \
    python3-venv>=3.13.3-1 \
    openssl>=3.5.0

COPY . /app
WORKDIR /app

RUN python3 -m venv /app/.venv \
    && . /app/.venv/bin/activate \
    && python3 -m pip install -r /app/requirements.txt

ENTRYPOINT ["/bin/bash", "--init-file", "/app/.venv/bin/activate", "-i"]

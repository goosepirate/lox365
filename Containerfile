FROM docker.io/library/python:3.8-slim
RUN python3 -m pip install --no-cache-dir \
  numpy \
  pytest \
  pytest-benchmark
RUN apt update && apt install -y \
  7zip \
  libreoffice-dev \
  && rm -rf /var/lib/apt/lists/*

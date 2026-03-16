# Use high-performance AI base image
FROM nvidia/cuda:12.2.0-base-ubuntu22.04

LABEL maintainer="Magne Vange"
LABEL role="AI Executive Advisor"
LABEL description="Full-Stack AI Compute Strategy Environment"

# Install system dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3.10 python3-pip git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /strategy

# Install core economic and compute dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy framework files
COPY . .

CMD ["/bin/bash"]

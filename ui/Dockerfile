FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        build-essential \
        curl && \
    rm -rf /var/lib/apt/lists/*

COPY combined_ca.pem /usr/local/share/ca-certificates/combined_ca.crt

RUN update-ca-certificates

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY pyproject.toml .

# Install project and dependencies
RUN pip install .

# Copy application
COPY ./src /app

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
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

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY pyproject.toml .

# Install project and dependencies
RUN pip install .

# Copy application (accidentally backed myself into a bad pattern here. Whoops)
COPY ./app /app/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

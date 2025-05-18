FROM python:3.11.8-slim as builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.11.8-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY ./app ./app

ENV PATH=/root/.local/bin:$PATH

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0:5000", "--workers", "4", "app.main:app"]
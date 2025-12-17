FROM python:3.11-slim

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src/ /app

COPY books.db /app

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8000/healthcheck || exit 1

CMD ["uvicorn", "book_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
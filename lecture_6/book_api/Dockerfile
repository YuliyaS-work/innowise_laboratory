FROM python:3.11-slim

RUN addgroup --system groupfastapi && adduser --system --ingroup groupfastapi userfastapi

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src/ /app

COPY books.db /app

RUN chown -R userfastapi:groupfastapi /app

USER userfastapi

EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8000/healthcheck || exit 1

CMD ["uvicorn", "book_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
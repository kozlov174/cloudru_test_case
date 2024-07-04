FROM python:3.12-alpine
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install fastapi
CMD ["uvicorn",  "api:app"]
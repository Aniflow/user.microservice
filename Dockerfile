FROM python:3.13.2-slim

WORKDIR /app

COPY app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8001

CMD ["python", "-m", "app.main"]
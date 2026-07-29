FROM python:3.12-slim

ENV PORT=4567

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "main.py"]

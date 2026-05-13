# TODO: Write Dockerfile for the consumer
#
# Requirements:
# - Base image: python:3.14-slim
# - Install pika from requirements.txt
# - Non-root USER
# - Start: python main.py

FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN useradd -m consumeruser
USER consumeruser

COPY main.py .
CMD ["python", "main.py"]  
"""
Exercise 03 — Event Consumer

Implement a RabbitMQ consumer that:
- Connects to RabbitMQ at RABBITMQ_URL env var
- Consumes messages from the "node_events" queue
- Logs each event to stdout: "EVENT: {event} | node: {node_name} | time: {timestamp}"
- Acknowledges each message after processing
"""

# TODO: Implement the consumer

import os
import pika 
from dotenv import load_dotenv

load_dotenv()
RABBITMQ_URL = os.getenv("RABBITMQ_URL")

def main():
    try:
        print(f"Connecting to RabbitMQ at {RABBITMQ_URL}", flush=True)
        connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        channel = connection.channel()
        channel.queue_declare(queue="node_events", durable=True)

        def callback(ch, method, properties, body):
            event_data = body.decode()
            print(f"EVENT: {event_data}", flush=True)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue="node_events", on_message_callback=callback)
        print("Waiting for messages...", flush=True)
        channel.start_consuming()
    except Exception as e:
        print(f"Error: {e}", flush=True)
        raise

if __name__ == "__main__":
    main()


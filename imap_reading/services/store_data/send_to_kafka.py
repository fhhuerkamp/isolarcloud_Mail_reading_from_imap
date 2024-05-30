from kafka import KafkaProducer
import json
from dotenv import load_dotenv
import os

"""
    Small Kafka producer for testing.
    Adapted from
    https://aiven.io/developer/teach-yourself-apache-kafka-and-python-with-a-jupyter-notebook

"""


def send_to_kafka(topic, payload):
    load_dotenv(override=False)
    host=os.environ.get("KAFKA_HOST")

    producer = KafkaProducer(
        bootstrap_servers=host,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    producer.send(
        topic,
        value = payload)

    producer.flush()
    return

if __name__ == "__main__":
    topic = "test_isolarcloud"
    payload = {
            "name": "fhh",
            "hotel": "Luxury Hotel",
            "dateFrom": "25-06-2021",
            "dateTo": "07-07-2021",
            "details": "I want the best room 😀😀😀😀😀!!!!"
            }
    send_to_kafka(topic, payload)

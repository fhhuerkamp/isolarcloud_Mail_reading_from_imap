from kafka import KafkaConsumer
import json
from dotenv import load_dotenv
import os


"""
    Small Kafka consumer for testing.
    Adapted from
    https://aiven.io/developer/teach-yourself-apache-kafka-and-python-with-a-jupyter-notebook

"""

def consumer(topic):
    load_dotenv(override=False)
    host=os.environ.get("KAFKA_HOST")
    consumer = KafkaConsumer(
        bootstrap_servers=host,
        value_deserializer = lambda v: json.loads(v.decode('ascii')),
        auto_offset_reset='earliest'
        )

    consumer.subscribe(topics=topic)
    for message in consumer:
        print ("%d:%d: v=%s" % (message.partition,
                          message.offset,
                          message.value))
    pass

if __name__ == "__main__":
    topic = "test_isolarcloud"

    consumer(topic)
    pass

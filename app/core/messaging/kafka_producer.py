import json
import os

from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9093")
KAFKA_TOPIC = "user-events"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def publish_event(event_data):
    producer.send(KAFKA_TOPIC, value=event_data)
    producer.flush()


def favorite_anime(user_id, anime_id):
    event_data = {
        'event': 'AnimeFavorited',
        'user_id': user_id,
        'anime_id': anime_id,
        'action': 'favorited',
        'timestamp': '2025-04-08T12:00:00Z'
    }

    publish_event(event_data)

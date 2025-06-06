import json
from aiokafka import AIOKafkaConsumer
from ..services.user_service import UserService
from ...config import CONFIG

KAFKA_BOOTSTRAP = CONFIG.KAFKA_BOOTSTRAP
TOPIC = "anime-events"
GROUP_ID = "anime-projection"


async def kafka_consume():
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        group_id=GROUP_ID,
        enable_auto_commit=True,
        auto_offset_reset="earliest"
    )

    await consumer.start()

    try:
        async for msg in consumer:
            event = json.loads(msg.value.decode("utf-8"))
            await UserService.user_favorited_event(event)
    finally:
        await consumer.stop()

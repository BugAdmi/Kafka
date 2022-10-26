from aiokafka import AIOKafkaConsumer


class Consumer:
    handle = None

    async def init(self, *args, **kwargs):
        self.handle = AIOKafkaConsumer(*args, **kwargs)

    async def star(self):
        await self.handle.start()

    async def stop(self):
        await self.handle.stop()

    async def __aiter__(self):
        async for msg in self.handle:
            yield msg


kfk_consumer = Consumer()

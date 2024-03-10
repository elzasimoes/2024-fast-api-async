import asyncio
from time import sleep


class SyncSpongeBob:
    """Classe síncrona simulando,
    recebendo o bob esponja como Event Loop enquanto prepara um hamburguer de Siri
    """

    def cook_bread(self):
        sleep(4)

    def cook_hamburguer(self):
        sleep(10)

    def mount_sandwich(self):
        sleep(4)

    def make_milkshake(self):
        sleep(4)

    def cook(self):
        self.cook_bread()
        self.cook_hamburguer()
        self.mount_sandwich()
        self.make_milkshake()


class AsyncSpongeBob:
    """Classe assíncrona simulando,
    recebendo o bob esponja como Event Loop enquanto prepara um hamburguer de Siri
    """

    async def cook_bread(self):
        await asyncio.sleep(4)

    async def cook_hamburguer(self):
        await asyncio.sleep(10)

    async def mount_sandwich(self):
        await asyncio.sleep(4)

    async def make_milkshake(self):
        await asyncio.sleep(4)

    async def make_sandwich(self):
        await asyncio.gather(self.cook_bread(), self.cook_hamburguer())
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())

    async def cook(self):
        await asyncio.gather(self.make_sandwich(), self.make_milkshake())
        await self.mount_sandwich()


sync_spongebob = AsyncSpongeBob()
asyncio.run(sync_spongebob.cook())

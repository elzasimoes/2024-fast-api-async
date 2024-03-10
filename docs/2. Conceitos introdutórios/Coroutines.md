### Sync e Async

- Sync
    - Sequencial;
    - Sempre apenas 1 tarefa em execução;
    - Se tiver que esperar por um processo o tempo é ocioso.

- Async 
    - Concorrente;
    - Mais de uma tarefa em execução;
    - Otimiza o tempo, durante o tempo de espera de um processo o programa vai trabalhar em outra tarefa.


- Event loop é quem vai osquestrar as funções assíncronas (Ex: Bob Esponja).
- Metodo gather permite que a gente execute as funções para serem executadas ao mesmo tempo, concorrendo entre sí;
- A função asyncio.gather em Python é usada para executar várias coroutines de forma concorrente. Permite que você agende várias tarefas assíncronas e aguarde até que todas estejam concluídas. A função gather é útil quando você precisa realizar várias operações assíncronas simultaneamente e aguardar até que todas sejam finalizadas;
- Executar funções de forma concorrente;

```python 
from time import sleep
import asyncio

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
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburguer()
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())
        
    async def cook(self):
        await asyncio.gather(
            self.make_sandwich(),
            self.make_milkshake()
        )
        await self.mount_sandwich()
        
sync_spongebob = AsyncSpongeBob()
asyncio.run(sync_spongebob.cook())

```

```bash
time python '/home/elza/introduction/intro/async_await_sponge_bob.py'
```

## Análise de performance

- Síncrona: 0m24.110s
- Assíncrona: 0m14.140s


## Melhorando a performance do projeto utilizando a programação assíncrona com aiohttp

```python

import aiohttp

url = f"https://v6.exchangerate-api.com/v6/e527e6c0460f230a08c74eea/pair/{from_currency}/{to_currency}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()

    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    

    exchange_rate = price * float(
        data['conversion_rate']
    )

    return exchange_rate

```



O aiohttp é uma biblioteca assíncrona para clientes e servidores HTTP. Ele é perfeito para operações de entrada/saída intensivas, como comunicação com APIs externas. No contexto deste projeto, o aiohttp é utilizado para realizar chamadas assíncronas a outras APIs.

Consulte o arquivo async_requests.py para exemplos de como integrar o aiohttp em sua aplicação FastAPI. Para obter informações detalhadas sobre o aiohttp, acesse aiohttp.readthedocs.io.


```bash
poetry add aiohttp
```

Exemplo

```python
import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.run(main())

```
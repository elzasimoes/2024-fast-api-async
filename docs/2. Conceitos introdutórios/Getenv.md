- Instalação do pacote

```bash
poetry new python-dotenv
```

- Configuração do arquivo .env

```.env
API_KEY=seu_valor_de_chave
DEBUG=True
```

- Importar para o código 

```python
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")

```


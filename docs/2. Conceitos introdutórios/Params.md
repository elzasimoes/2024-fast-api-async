### Parâmetros de Caminho (Path Parameters):

- São incorporados diretamente na própria URL (end-point). Exemplo:

```python
@router.get('/converter/{from_currency}}')
def converter(from_currency: str):
    return "It Works"
```

### Parâmetros de Consulta (Query Parameters)

- São usados para passar dados na URL após o ponto de interrogação.


```http
  GET http://127.0.0.1:5000/converter/v1/async/USD?to_currencies=BRL,USD&price=1.90
```

```http
  GET http://127.0.0.1:5000/converter/v1/USD?to_currencies=BRL,USD&price=1.90
```

### Parâmetros no Corpo da Requisição (Request Body):

- São usados para enviar dados no corpo da requisição, geralmente em formato JSON.

### Parâmetros em Cabeçalhos (Headers):

- Podem ser acessados diretamente como argumentos da função de rota.


## Exemplo de uso com FastAPI

```python

from fastapi import Path, Query

@router.get("/{from_currency}")
def sync_converter_router(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
    to_currencies: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"),
    price: float = Query(ge=0),
):

```
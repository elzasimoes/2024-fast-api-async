from asyncio import gather

from fastapi import APIRouter, Path, Query

from converter_api.converter import async_converter, sync_converter
from converter_api.schemas import ConverterInput, ConverterOutput

router = APIRouter(prefix="/converter/v1")


@router.get("/{from_currency}")
def sync_converter_router(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
    to_currencies: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"),
    price: float = Query(ge=0),
):
    """Rota síncrona

    Query:
        /converter/v1/USD?to_currencies=BRL,GBP&price=1.90

    Args:
        from_currency (str): A moeda, ex: BRL ou USD
        to_currencies (str): A modela, ex: BRL ou USD
        price (float): O valor a ser convertido

    Returns:
        _float_: O Valor convertido
    """
    to_currencies = to_currencies.split(",")

    result = []

    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency, to_currency=currency, price=price
        )

        result.append(response)

    return result


@router.get("/async/{from_currency}")
async def async_converter_router(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
    to_currencies: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"),
    price: float = Query(ge=0),
):
    """
    Rota assíncrona

    Query:
        /converter/v1/USD?to_currencies=BRL,GBP&price=1.90

    Args:
        from_currency (str): A moeda, ex: BRL ou USD
        to_currencies (str): A modela, ex: BRL ou USD
        price (float): O valor a ser convertido

    Returns:
        _float_: O Valor convertido
    """
    to_currencies = to_currencies.split(",")

    coroutines = []

    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency, to_currency=currency, price=price
        )

        coroutines.append(coro)

    result = await gather(*coroutines)

    return result


@router.get("/async/base_model/{from_currency}", response_model=ConverterOutput)
async def async_converter_router_body(
    body: ConverterInput, from_currency: str = Path(max_length=50, regex="^[A-Z]{3}$")
):
    """
    Rota assíncrona com Pydantic para validação dos dados e Body

    Query:
        GET /converter/v1/async/base_model/BRL

    Example:
    ```json
    {
        "price": 1,
        "to_currencies": ["USD"]
    }
    ```

    Args:
        from_currency (str): A moeda, ex: BRL ou USD
        
    Returns:
        response_model(json): Os valores convertidos
    """
    to_currencies = body.to_currencies
    price = body.price

    coroutines = []

    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency, to_currency=currency, price=price
        )

        coroutines.append(coro)

    result = await gather(*coroutines)

    return ConverterOutput(message="success", data=result)

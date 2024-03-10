from dotenv import load_dotenv
import os
import aiohttp
import requests
from fastapi import HTTPException

load_dotenv()

API_KEY = os.getenv('API_KEY')


def sync_converter(from_currency: str, to_currency: str, price: float):
    """Essa função fará uma requisição síncrona HTTP para uma api https://www.alphavantage.co,
        que retorna a conversão dos valores das moedas

    Args:
        from_current (str): Moeda de origem
        to_current (str): Moeda convertida
        price (float): Valor a ser convertido

    Raises:
        1. HTTPException: Erro na requisição retornando 400
        2. HTTPException: Erro na conversão retornando 400

    Returns:
        _float_: Preço * o valor convertido
    """

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}"
    
    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)

    data = response.json()

    if data["result"] == "error":

        raise HTTPException(status_code=400, detail=data["error-type"])

    exchange_rate = price * float(data["conversion_rate"])

    return exchange_rate


async def async_converter(from_currency: str, to_currency: str, price: float):
    """Essa função fará uma requisição assíncrona HTTP para uma api https://www.alphavantage.co,
        que retorna a conversão dos valores das moedas

    Args:
        from_current (str): Moeda de origem
        to_current (str): Moeda convertida
        price (float): Valor a ser convertido

    Raises:
        1. HTTPException: Erro na requisição retornando 400
        2. HTTPException: Erro na conversão retornando 400

    Returns:
        _float_: Preço * o valor convertido
    """
 
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
              
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)

    if data["result"] == "error":

        raise HTTPException(status_code=400, detail=data["error-type"])

    exchange_rate = price * float(data["conversion_rate"])

    return {to_currency: exchange_rate}

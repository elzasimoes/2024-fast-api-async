import re
from typing import List

from pydantic import BaseModel, Field, validator


class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @validator("to_currencies")
    def validate_to_currencies(cls, value):
        """Validar o campo "to_currencies" utlizando o decorator @validator

        Args:
            value (str): Valor ser validado

        Raises:
            ValueError: Retorna um ValueError caso o valor não seja atendido

        Returns:
            value (str): Retorna o valor validado
        """

        for currency in value:
            if not re.match("^[A-Z]{3}$", currency):
                raise ValueError(f"Invalid currency {currency}")
        return value


class ConverterOutput(BaseModel):
    message: str
    data: List[dict]

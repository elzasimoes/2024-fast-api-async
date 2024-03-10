- Pydantic é uma biblioteca Python para validação de dados usando o sistema de tipos do Python. 

- [Documentação do Pydantic](https://docs.pydantic.dev/latest/)

- Utilizar Pydantic para trabalhar com dados é fundamental no corpos de Requisição


- Data Models: Pydantic permite a definição de modelos de dados usando classes Python normais, aproveitando as dicas de tipo para descrever a estrutura dos dados.
- As dicas de tipo no Pydantic são implícitas e inferidas a partir das atribuições nos modelos, evitando a necessidade de duplicação de informações.
- Validação Automática: Pydantic realiza validação automática dos dados com base nos tipos declarados, garantindo que os dados estejam de acordo com as expectativas do modelo
- Serialização Automática com @validator: Além da validação de entrada, Pydantic facilita a serialização de dados, convertendo automaticamente instâncias de modelos em representações de dados compatíveis.
- Geração de Schemas: Pode gerar automaticamente esquemas JSON e OpenAPI (usando o padrão OpenAPI 2 e 3) a partir dos modelos, facilitando a interoperabilidade com outros sistemas
- Suporte a Campos Opcionais: Permite a definição de campos opcionais em modelos, que podem ser ausentes nos dados e têm um valor padrão.


- Sem Pydantic:

```json
user = {
    "name": "João",
    "age": 23,
    "email" "teste@gmail.com"
}
```

- Com Pydantic

```python

from pydantic import BaseModel, validator 

class User(BaseModel):
    name: str,
    age: int,
    email: str

    @validator('email')
    def validate_email(cls, value):
        if '@' not in email:
            raise ValueError('Invalid Email')
        return value

user = user(name="João", age=23, email="teste@gmail.com")

```
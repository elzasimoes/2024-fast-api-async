- Dicas de tipo, ou "type hints", são anotações usadas em Python para indicar o tipo de uma variável, parâmetro de função ou valor de retorno de função. Elas não são aplicadas pelo interpretador Python em tempo de execução, mas servem como uma forma de documentação e podem ser verificadas estaticamente por ferramentas como linters ou o mypy. As dicas de tipo foram introduzidas no PEP 484 e fazem parte de uma iniciativa mais ampla para adicionar tipagem estática ao Python, muitas vezes chamada de "type hints" ou "type annotations".

```python
def hello_world(name: str) -> str:
    return 'Hello World {name}'
```




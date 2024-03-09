- TDD (Test Driven Development)
- Async/await em detalhes
- Docker e dockerização de aplicação
- Utilizar path, query e body parameter
- Segurança e Autenticação em FastAPI
- Trabalhar com validações avançadas
- Testes unitários com Pytest
- Trabalhar com Pydantic
- Trabalhar com PostgreSQL
- Fazer CRUD com SQLAlchemy
- Migrations com alembic
- Integração com API externa


## Instalação do WLS para configuração de Ambiente de Desenvolvimento

- No Powershell em modo de administrador digite o seguinte comando:

``wsl -- install``

## Guia de Instalação do WLS

- https://learn.microsoft.com/pt-br/windows/wsl/
- https://learn.microsoft.com/pt-br/windows/wsl/install

- Configurar Ubuntu como padrão

``wsl --set-default Ubuntu``

## Instalação do Pyenv na WLS

- Comandos de configuração do Pyenv
- https://roasted-basil-9d8.notion.site/Pyenv-pt-0410a3d9ce594cc99a7fb7ca954aee52

``
# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
``

## Utilização do Vim para configuração dos path de ambiente na WLS

sudo apt-get update
sudo apt-get vim
- :wq salvar
- o pular linha

- Comandos básicos VIM: https://openwebinars.net/blog/vim-manual-de-uso-basico/

``vim ~/.bashrc``

### Instalação do Poetry na WLS

``curl -sSL https://install.python-poetry.org | python3 -``

- Configurar o path

``export PATH="$HOME/.local/bin:$PATH``

## Configuração e instalação do Docker no Windows x WLS

- https://docs.docker.com/desktop/wsl/

- Instalar o Docker Desktop com permissão de uso WLS
- Configuração do Docker para uso no WLS Resource -> WLS Integration -> Ubuntu
- Verificar se o docker está funcionando no WLS - Ubuntu

``docker ps``

## Configuração do VSCODE

- Download Plugin WLS
- Iniciar o VSCode pelo WLS utilizando code .


# Iniciando projeto com Poetry

``poetry init``
``poetry shell`` iniciar ambiente virtual
``poetry add pydantic``
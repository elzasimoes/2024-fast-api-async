# Iniciando a preparação de ambiente

## Instalação do WSL para configuração do ambiente de desenvolvimento Linux

- No Powershell em modo de administrador digite o seguinte comando para instalação do WSL:

```bash
  wsl -- install
```

## Guia de Instalação do WSL

- [Documentação do Subsistema Windows para Linux](https://learn.microsoft.com/pt-br/windows/wsl/) 
- [Como instalar o Linux no Windows com o WSL](https://learn.microsoft.com/pt-br/windows/wsl/install)  

- Em seguida envie o seguinte comando para configurar Ubuntu como distro padrão:

```bash
  wsl --set-default Ubuntu
```

## Utilização do Vim para configuração dos path de ambiente na WSL

```bash
sudo apt-get update
```
```bash
sudo apt-get vim
```

 - [Comandos Básicos VIM](https://openwebinars.net/blog/vim-manual-de-uso-basico/)

## Instalação do Pyenv na WLS (Similar ao virtualenv):

- Comandos de configuração do Pyenv

- Garanta que todas dependências necessárias estão instaladas

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
- Baixe e execute o script de instalação

```bash
curl https://pyenv.run | bash
```

- Adicione o seguinte script no arquivo ~/.bashrc

```bash
vim ~/.bashrc
```

```bash
# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

## Instalação do Poetry na WLS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

- Configurar o path

```bash
vim ~/.bashrc
```

```bash
export PATH="$HOME/.local/bin:$PATH
```

## Configuração e instalação do Docker no Windows x WLS

- [Docker Desktop WSL 2 backend on Windows](https://docs.docker.com/desktop/wsl/)

- Instalar o Docker Desktop com permissão de uso WLS
- Configuração do Docker para uso no WLS Resource -> WLS Integration -> Ubuntu
- Verificar se o docker está funcionando no WLS - Ubuntu

```bash
docker ps
```

## Configuração do Vscode

- Download Plugin WLS Version: 0.86.0

```bash
Name: WSL
Id: ms-vscode-remote.remote-wsl
Description: Open any folder in the Windows Subsystem for Linux (WSL) and take advantage of Visual Studio Code's full feature set.
Version: 0.86.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl
```

- Iniciar o VSCode pelo WLS utilizando:

```bash
elza@DESKTOP-GSPLJUA:~/introduction$ code .
```

- Instalar os plugins necessários no VScode WLS

``Python
Pylance
Gitleans``


# Iniciando projeto com Poetry

```bash
poetry init
```

- Iniciar ambiente virtual

```bash
poetry shell
```

- Adicionar um pacote

```bash
poetry add pydantic
```

- Verificar onde está o ambiente virtual

```bash
poetry env info -p
```

```output
/home/elza/.cache/pypoetry/virtualenvs/introduction-1CFmuCEW-py3.10\bin\python
```

- CTRL + Shift + P > Select Interpreter > Path para entrar no ambiente virtual





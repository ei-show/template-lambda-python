# template-lambda-python
Template for developing using python with AWS lambda.

## Setup

### First time only

```sh
pyenv install 3.12.1
pyenv local 3.12.1
python3 --version
python3 -m venv .venv
source .venv/bin/activate # bash/zsh
# source .venb/bin/activate.fish # fish
python3 -m pip install --upgrade pip
pip3 install -r ./requirements.txt
deactivate
```

### Second and subsequent times

```sh
pyenv install $(cat .python-version)
python3 --version
python3 -m venv .venv
source .venv/bin/activate # bash/zsh
# source .venb/bin/activate.fish # fish
python3 -m pip install --upgrade pip
pip3 install -r ./requirements.txt
deactivate
```

## Local tests

```sh
python-lambda-local lambda_function.py -f lambda_handler tests/event.json
```
# Myapp: A CLI Application.

## Description:

Built on:
Python3 - 3.11.9
Mac

## Commands

- `myCommand TITLE DESCRIPTION` : myCommand does something

## Install

```bash
pip3 install git+https://github.com/username/myapp
```

## Usage:

`

## Setup source code

The following steps are for cloning, modifying, testing the code.

- Clone

```bash
git clone git@github.com:username/myapp.git
```

- Setup virtual env

```bash
python3 -m venv venv
source ./venv/bin/activate
```

- Install Requirements

```bash
pip3 install -r requirements.txt
```

- Run CLI

```bash
python3 app/main.py [OPTIONS] COMMAND [ARGS]
```

- Run tests

```bash
pytest
```

- Debugging
  If running the tests creates a "ModuleNotFoundError", run the following command in your virtual env.

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/app
```

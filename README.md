# Billing Automation Application.

## Description:

This python application runs Gmail APIs to read bills, process them, and optionally create new Venmo Requests to other

Built on:
Python3 - 3.11.9
Mac

## Install

```bash
pip3 install git+https://github.com/username/myapp
```

## Usage:

## Setup source code

The following steps are for modifying and testing the code.

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
python3 app/main.py
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

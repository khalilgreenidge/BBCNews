﻿# Recommender

## Requirements
- Must have Python installed. At least 3.6

## Getting started
This project utilises **_virtualenv_**, which we will use for our dependencies.
This enables multiple side-by-side installation of Python, one for each project. 
Learn more about _virtualenv_ [here](https://flask.palletsprojects.com/en/0.12.x/installation/#virtualenv).

1. Create a virtual environment

```shell
python -m venv
```

2. Activate `virtualenv`

```shell
. venv/bin/activate
```

3. Install the dependencies

```shell
pip install -r requirements.txt
```

4. Run the server

```shell
uvicorn main:app 
```

You can also view the docs by going to [localhost:8000/redocs](http://localhost:8000/redocs)







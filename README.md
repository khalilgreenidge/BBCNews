# Recommender

## Requirements
- Must have Python installed. At least 3.6

## Getting started
This project utilises **_virtualenv_**, which we will use for our dependencies.
This enables multiple side-by-side installation of Python, one for each project. 
Learn more about _virtualenv_ [here](https://flask.palletsprojects.com/en/0.12.x/installation/#virtualenv).

### 1. Create a virtual environment. 

_P.s if you're using a Windows WSL terminal, you need to run this in a command line terminal_.

```shell
python -m venv
```
_Manual Alternative_

I personally prefer to manually create a new virtual env in PyCharm so that it is recognised
when running tests etc. Follow this handy [guide](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env) from Jetbrains.

### 2. Activate `virtualenv`

If you're using a linux terminal, run:
```shell
. venv/bin/activate
```

If you're using windows terminal, run:

```shell
. venv/scripts/activate
```

_Manual Alternative_

If you created a virtual env via PyCharm, you can skip this step because PyCharm would have activated it for you once you create it manually.

### 3. Install the dependencies

```shell
pip install -r requirements.txt
```

_Manual Alternative_

Once you create the new virtual environment in PyCharm, it automatically picks up that you 
have a `requirements.txt` file. You will see a popup with a yellow background asking you to _"install dependencies"_.

### 4. Run the server

```shell
uvicorn main:app 
```

You can also view the docs by going to [localhost:8000/redocs](http://localhost:8000/redocs)


# Testing

Once you have install all of the dependencies properly, PyCharm should 
have auto-dected `pytest` in your `venv/lib` folder. If not you can follow
this [guide](https://www.jetbrains.com/help/idea/pytest.html#enable-pytest) to set `pytest` as the default test runner.
Afterwards, a green play button should have appeared.





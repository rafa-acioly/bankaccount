# Bank Acount

## How to Install:

1. Download and upgrade pip
    - [python3 -m ensurepip --upgrade](https://pip.pypa.io/en/stable/)
2. Create a virtual environment and activate it
    - [python3 -m venv venv](https://docs.python.org/3/tutorial/venv.html)
    - source venv/bin/activate
2. Install the dependencies:
    - [python3 -m pip install -r requirements.txt](https://pip.pypa.io/en/stable/installing/)


## Running the application:
```
@python3 -m uvicorn api.api:app --reload
```

## Acessing the docs:
After running the app, you can access the docs by visiting the URL: `http://localhost:8000/docs`
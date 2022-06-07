from http import HTTPStatus
from typing import Union
from fastapi import FastAPI, Response

from schemas import EventRequest
from tools import actions

app = FastAPI()


@app.post("/reset")
async def reset():
    actions.get("reset")()
    return 'OK'


@app.get("/balance", status_code=HTTPStatus.OK)
async def balance(response: Response, account_id: Union[str, None] = None):
    balance = actions.get("balance")(account_id)
    if not balance:
        response.status_code = HTTPStatus.NOT_FOUND
        return 0

    return balance


@app.post("/event", status_code=HTTPStatus.CREATED)
async def event(request: EventRequest, response: Response):
    action_succeded = actions.get(request.type)(request)
    if not action_succeded:
        response.status_code = HTTPStatus.NOT_FOUND
        return 0
    
    return action_succeded
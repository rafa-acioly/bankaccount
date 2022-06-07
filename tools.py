from functools import partial
from typing import Dict
from collections import defaultdict
from typing import Callable
from schemas import EventRequest


"""
A fake database of accounts.
"""
_accounts = defaultdict(partial(defaultdict, int))


def reset():
    _accounts.clear()


def balance(account_id: str) -> int:
    return _accounts[account_id]["amount"]


def deposit(content: EventRequest) -> dict:
    _accounts[content.destination]["amount"] += content.amount

    return {
        "destination": {
            "id": content.destination,
            "balance": _accounts[content.destination]["amount"]
        }
    }


def withdraw(content: EventRequest) -> dict:
    if not content.origin in _accounts.keys():
        return 0

    _accounts[content.origin]["amount"] -= content.amount

    return {
        "origin": {
            "id": content.origin,
            "balance": _accounts[content.origin]["amount"]
        }
    }


def transfer(content: EventRequest) -> dict:
    if not content.origin in _accounts.keys():
        return 0

    _accounts[content.origin]["amount"] -= content.amount
    _accounts[content.destination]["amount"] += content.amount

    return {
        "origin": {
            "id": content.origin,
            "balance": _accounts[content.origin]["amount"]
        },
        "destination": {
            "id": content.destination,
            "balance": _accounts[content.destination]["amount"]
        }
    }


"""
A map of event types to their respective handlers.
"""
actions: Dict[str, Callable] = {
    "deposit": deposit,
    "withdraw": withdraw,
    "transfer": transfer,
    "balance": balance,
    "reset": reset
}
from dataclasses import dataclass


@dataclass
class Proxy:
    pass


@dataclass
class TelegramAccount:
    api_id: int
    api_hash: str
    session_token: str
    phone: str | None
    bot_token: str | None
    proxy: list | None


@dataclass
class BalancingObject:
    torsion_object: str | Proxy | TelegramAccount
    num_requests: int

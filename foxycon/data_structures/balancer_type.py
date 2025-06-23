from dataclasses import dataclass


@dataclass
class BalancerType:
    num_requests: int | None
    num_usage_skips: int | None
    status_block: bool | None


@dataclass
class Proxy(BalancerType):
    proxy_str: str

    def __str__(self):
        return "proxy"


@dataclass
class InstagramAccount(BalancerType):
    login: str
    password: str
    token_session: str | None
    initialization_status: bool | None

    def __str__(self):
        return "instagram_account"


@dataclass
class TelegramAccount(BalancerType):
    api_id: int
    api_hash: str
    token_session: str | None
    initialization_status: bool | None

    def __str__(self):
        return "telegram_account"

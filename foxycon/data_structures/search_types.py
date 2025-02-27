from datetime import datetime
from dataclasses import dataclass

from foxycon.data_structures.statistician_type import TelegramChatData


@dataclass
class TgStatMessage:
    telegram_chat_data: TelegramChatData
    link_message: str
    date_publication: datetime
    message: str
    views: int


@dataclass
class TelegramUserData:
    user_id: int
    bot: bool
    first_name: str | None
    last_name: str | None
    username: str | None

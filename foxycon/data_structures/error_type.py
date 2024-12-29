from enum import Enum


class Telegram(Enum):
    NoError = 'None'
    PostNotFound = 'Пост не найден'
    UserPrivacyRestrictedError = 'Не удалось вступить в канал: ограничение конфиденциальности'
    ChatWriteForbiddenError = 'Не удалось вступить в канал: доступ запрещён'
    JoinChannelRequestSend = 'Канал приватный. Отправлена заявка на вступление в канал'
    FloodWaitError = 'Слишком много запросов. Необходимо подождать'
    General = 'Общая ошибка: '

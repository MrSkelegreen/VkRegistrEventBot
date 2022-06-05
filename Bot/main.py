from Bot import Bot

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
# токен группы
session = vk_api.VkApi(token="")
session_api = session.get_api()
# id группы
groupId = ""
longpool = VkBotLongPoll(session, groupId)


def sendMessage(id, text):
    session.method("messages.send", {"user_id": id, "message": text})


bot = Bot()

for event in longpool.listen():
    if event.type == VkBotEventType.GROUP_JOIN:
        id = event.obj.user_id
        # текст сообщения
        text = ""

        bot.send_message(receiver_user_id=id, message_text=text)

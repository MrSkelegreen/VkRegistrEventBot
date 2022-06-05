import vk_api
from vk_api.utils import get_random_id

# токен пользователя и его id
ACCESS_TOKEN = ""
USER_ID = ""


class Bot:

    vk_session = None

    vk_api_access = None

    authorized = False

    def __init__(self):

        self.vk_api_access = self.do_auth()

        if self.vk_api_access is not None:
            self.authorized = True
        # пользователь, которому отправляются сообщения по-умолчанию
        self.default_user_id = ""

    def do_auth(self):
        token = ACCESS_TOKEN
        try:
            self.vk_session = vk_api.VkApi(token=token)
            return self.vk_session.get_api()
        except Exception as error:
            print(error)
            return None

    def send_message(self, receiver_user_id: str = None, message_text: str = "сообщение по-умолчанию"):

        if not self.authorized:
            print("Unauthorized. Check if ACCESS_TOKEN is valid")
            return

        if receiver_user_id is None:
            receiver_user_id = self.default_user_id

        try:
            self.vk_api_access.messages.send(user_id=receiver_user_id, message=message_text, random_id=get_random_id())
            print(f"Сообщение отправлено для ID {receiver_user_id}")
        except Exception as error:
            print(error)

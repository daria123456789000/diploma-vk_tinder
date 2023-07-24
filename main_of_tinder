др варик
from vk_api.longpoll import VkEventType, VkLongPoll
from tokens import main_token

vk_session = vk_api.VkApi(token = main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
if event.type == VkEventType.MESSAGE_NEW and event.to_me:
if event.to_me:
vk = vk_session.get_api()
msg = event.text.lower()
id = event.user_id
user_get = vk.users.get(user_ids =id)
user_get = user_get[0]

if msg == "Привет!" :
sender(id, "Привет, Саша!") 
хня

норм 
2
from repository.repository import Repository
from vkbot.vk_bot import VK_Bot
import vk_api

import os.path

def get_vk_token():
    path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "resources", "vkinder_key.ini"))
        
 with open(path, "r") as file:
        return file.read()

def main():
    vk_token = get_vk_token()
    vk_session = vk_api.VkApi(token='token')
    vk = vk_session.get_api()
    response = vk_session.method('users.search', {
                                 'q': 'Хворостова Саша', 'sex': 0, 'age_from': 2, 'age_to': 35, 'hometown': 'Сибирь'})
    print(response)
    return

    storage = Storage()
    print(storage.get_storage_user())


if __name__ == "__main__":
    vk_bot = VK_Bot(get_vk_token())


class VKinder:
    URL_AUTH = "https://oauth.vk.com/authorize"
    URL_REDIRECT = "https://oauth.vk.com/blank.html"
    URL_USER_PAGE = "https://vk.com/id"
    db_session = None
    vk_session = None
    vk_group_session = None
    user_info = {}

    def __init__(self,
                 my_token: str = None,
                 group_token: str = None,
                 user_id: str = None,
                 db_login: str = None,
                 db_password: str = None,
                 db_name: str = None,
                 db_localhost: int = 5432,
                 app_id=None,
                 group_id=None,
                 users_count_per_inquiry=10,
                 inquiry_counts=0
                 ):
        self.token = my_token
        self.group_token = group_token
        self.user_info["user_id"] = user_id
        self.db_login = db_login
        self.db_password = db_password
        self.db_name = db_name
        self.db_localhost = db_localhost
        self.APP_ID = app_id
        self.GROUP_ID = group_id
        self.users_count_per_inquiry = users_count_per_inquiry
        self.inquiry_counts = inquiry_counts


def event_handler(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
                if event.text.lower() == 'привет':
                    '''Логика для получения данных о пользователе'''
                    self.params = self.vk_tools.get_profile_info(event.user_id)
                    self.message_send(
                        event.user_id, f'Привет, {self.params["name"]}! Я робот-помощник. Помогу найти вам пару. Для этого введите команду "ПОИСК" или "S"')
                elif event.text.lower() == 'поиск' or event.text.lower() == 's':
                    '''Логика для поиска анкет''' 
                    self.message_send(
                        event.user_id, 'Начинаю поиск')
                    if self.worksheets:
                        worksheet = self.worksheets.pop()
                        photos = self.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:
                            photo_string += f'photo{photo["owner_id"]}_{photo["id"]},'
                    else:
                        self.worksheets = self.vk_tools.search_worksheet(
                            self.params, self.offset)

                        worksheet = self.worksheets.pop()
                        
'добавление анкеты в бд согласно event.user_id'

                elif event.text.lower() == 'пока':
                    self.message_send(
                        event.user_id, 'До скорой встречи')
                else:
                    self.message_send(
                        event.user_id, 'Нераспознанная команда')

                        


#метод получения фото
    def get_photos(self, user_id):
    photos_params = {'owner_id': user_id,
                        'album_id': 'profile',
                        'rev': '1',
                        'access_token': self.access_token,
                        'extended': '1',
                        'v': '5.131'}
    try:
        photos_response = requests.get(
            'https://api.vk.com/method/photos.get', params=photos_params)
        photos_result = photos_response.json()
        photo_urls = []
        if 'response' in photos_result:
            photos = photos_result['response']['items']
            sorted_photos = sorted(photos, key=lambda x: x.get('likes', {}).get(
                'count', 0), reverse=True)  # Сортировка по лайкам
            for photo in sorted_photos[:3]:
                photo_urls.append(photo['sizes'][-1]['url'])
        return photo_urls
    except Exception as e:
        print(f"Ошибка при получении фотографий: {e}")
        return []


 def _search_pair(self, user_id: int, next_user_state: int):
        if self.test_mode:
            self._send_message(user_id, '_search_pair()')
        self._check_new_user(user_id)
        if not self.repository.has_user_condition_exists(user_id):
            self._send_message(user_id, "Search condition isn't exists")
            return False
        conditions = self.repository.get_search_conditions(user_id)
        # self._search_pair_with_conditions(user_id, conditions)
        # params = {'user_id': user_id}
        params = dict()
        params['count'] = 5
        params['fields'] = 'first_name,last_name,sex,bdate,home_town,photo_50,relation'
        params['sex'] = conditions['sex']
        params['status'] = conditions['relation']
        params['age_from'] = conditions['age_from']
        params['age_to'] = conditions['age_to']
        if conditions.get('city'):
            params['hometown'] = conditions['city']

        search_result = self.vkuser_session.method('users.search', params)

        results_to_save = search_result["items"]
        

        def _database_auth(self):
        DSN = f"postgresql://{self.db_login}:{self.db_password}@localhost:{self.db_localhost}/{self.db_name}"
        engine = sq.create_engine(DSN)

        db.create_tables(engine)

        Session = sessionmaker(bind=engine)
        self.db_session = Session()

        

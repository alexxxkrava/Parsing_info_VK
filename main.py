import json
import requests
import os.path
from pprint import pprint

class VkUser:

    url = 'https://api.vk.com/method/'

    def __init__(self, token):
        self.params = {
            'access_token': token,
            'v': '5.131'
        }

    def user_info(self, user_id):
        info_params = {
            'user_ids': user_id,
            'fields' : 'online, bdate, sex, relation, career'
        }

        URL = self.url + 'users.get'

        res = requests.get(URL, params={**self.params, **info_params}).json()
        return res

    def get_photo(self, user_id):
        photo_params = {
            'user_ids': user_id,
            'fields': 'photo_max_orig'
        }

        URL = self.url + 'users.get'

        res = requests.get(URL, params={**self.params, **photo_params}).json()["response"][0]["photo_max_orig"]
        link_photo = requests.get(res).content

        with open('user_photo.jpg', 'wb') as file:
            file.write(link_photo)

    def get_json(self, user_id):
        if not os.path.exists(r'C:\Users\Алексей\Desktop\Погода Локня\test.json'):
            with open('test.json', 'w', encoding='UTF-8') as f:
                json.dump(self.user_info(user_id), f, indent=4, ensure_ascii=False)
        else:
            pass
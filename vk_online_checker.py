import os
import requests
import datetime
from dotenv import load_dotenv


load_dotenv()


def info_about_user(target_id: str):
    ACCESS_TOKEN = os.getenv('VK_ACCESS_TOKEN')
    API_VERSION = '5.124'
    URL = f'https://api.vk.com/method/users.get?user_ids={target_id}&fields=online,last_seen' \
          f'&access_token={ACCESS_TOKEN}&v={API_VERSION}'

    response = requests.request('GET', URL)

    try:
        target_name = response.json()['response'][0]['first_name'] + ' ' + response.json()['response'][0]['last_name']
        target_status = 'online' if response.json()['response'][0]['online'] else 'offline'
        target_last_seen = response.json()['response'][0]['last_seen']['time']

        date_time = datetime.datetime.fromtimestamp(target_last_seen)
        time = date_time.strftime('%H:%M:%S')

        return target_name, target_status, time

    except KeyError:
        return 'Invalid user ID or something wrong.'

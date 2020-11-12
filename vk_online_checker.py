""" Напиши программку, которая мониторит онлайн-статус друга и посылает тебе SMS, когда друг появляется онлайн.
Запросы к ВК API можно делать напрямую, а можно найти специальную библиотеку, как это было в случае с Twilio.
На твой выбор. """


def vk_online_checker(target_id: str):
    global app_working  # to exit from cycle while
    global message_sent

    load_dotenv()

    # setting up logs
    logging.basicConfig(filename='vk_online_checker.log',
                        level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(message)s')

    target_id = str(target_id)

    # constants
    ACCESS_TOKEN = os.getenv('VK_ACCESS_TOKEN')
    API_VERSION = "5.124"
    URL = "https://api.vk.com/method/users.get?user_ids=" + target_id + "&fields=online,last_seen&access_token=" + ACCESS_TOKEN + "&v=" + API_VERSION

    # request
    response = requests.request("GET", URL)

    # selection of information
    try:
        target_name = response.json()['response'][0]['first_name'] + ' ' + response.json()['response'][0]['last_name']
        target_status = 'online' if response.json()['response'][0]['online'] else 'offline'
        target_last_seen = response.json()['response'][0]['last_seen']['time']
    except KeyError:
        return send_sms('Неверный ID пользователя или что-то пошло не так.')

    if target_status == 'online':
        app_working = False
        return send_sms(f'{target_name} в сети.')

    if target_status == 'offline' and not message_sent:
        date_time = datetime.datetime.fromtimestamp(target_last_seen)
        time = date_time.strftime('%H:%M:%S')
        message_sent = True
        return send_sms(f'{target_name} не в сети. Последний визит в {time}. Я продолжу наблюдение и сообщу, '
                        f'когда {target_name} появится в сети.')


if __name__ == '__main__':
    import os
    import logging
    import requests
    import datetime
    from time import sleep
    from dotenv import load_dotenv

    from send_sms import send_sms

    app_working = True
    message_sent = False

    while app_working:
        vk_online_checker('Put person ID here')
        sleep(60)

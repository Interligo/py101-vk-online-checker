""" Напиши программку, которая мониторит онлайн-статус друга и посылает тебе SMS, когда друг появляется онлайн.
Запросы к ВК API можно делать напрямую, а можно найти специальную библиотеку, как это было в случае с Twilio.
На твой выбор. """

import logging
from time import sleep

from send_sms import send_sms
from vk_online_checker import info_about_user


if __name__ == '__main__':
    target_id = input('Please put person ID here: ')
    logging.info(f'User tried to test {target_id} ID.')

    try:
        target_name, target_status, last_seen_time = info_about_user(target_id)

        if target_status == 'offline':
            send_sms(f'{target_name} is offline. Last seen at {last_seen_time}. I will continue to monitoring and '
                     f'will notify when {target_name} will appeared online.')
            logging.info(f'{target_name} is offline. Last seen at {last_seen_time}.')

        while True:
            target_name, target_status, last_seen_time = info_about_user(target_id)

            if target_status == 'online':
                send_sms(f'{target_name} is online.')
                logging.info(f'{target_name} is online.')
                break
            else:
                sleep(60)

    except ValueError:
        print('Invalid user ID. Please run app again.')
        logging.info('User entered wrong ID.')

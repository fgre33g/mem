import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from picks import pickss, iq

vk_session = vk_api.VkApi(token='8b42238a2cba473982dfffff8b0530c19903f56165b797ec888e16501a82483e0365164cd4aedcb3febec')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text
        if event.from_user and not event.from_me:
            if response.find('Пошел нахуй') != -1 \
                    or response == "Пошел на хуй" \
                    or response == "Пнх":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id,
                                   'message': 'Сам иди!',
                                   'random_id': 0})

            elif response == "Люблю тебя":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id,
                                   'message': 'А я тебя люблю',
                                   'random_id': 0})

            elif response == "Ику" or \
                    response == "Мой iq" \
                    or response == "iq" \
                    or response == "Iq" \
                    or response == "Айкью":
                vk_session.method('messages.send', {'user_id': event.user_id,
                                                    'message': 'Твой iq ' + str(random.choice(iq)),
                                                    'random_id': 0})
            elif response.find('Мем') != -1 \
                    or response.find('мем') != -1 \
                    or response.find('Мемы') != -1 \
                    or response.find('мемы') != -1:
                vk_session.method('messages.send', {'user_id': event.user_id,
                                                    'message': 'Кто-то сказал MEM?\nНу лови))))',
                                                    'random_id': 0,
                                                    'attachment': 'photo66105035_' + str(random.choice(pickss))})
        elif event.from_chat and not event.from_me:
            if response == "Пошел нахуй" \
                    or response == "Пошел на хуй" \
                    or response == "Пнх":
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': 'Сам иди!',
                                   'random_id': 0})
            elif response == "Люблю тебя":
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': 'А я тебя люблю',
                                   'random_id': 0})
            elif response == "Ику" \
                    or response == "Мой iq" \
                    or response == "iq" or \
                    response == "Iq" or \
                    response == "Айкью":
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': 'Твой iq ' + str(random.choice(iq)),
                                   'random_id': 0})
            elif response.find('Мем') != -1 \
                    or response.find('мем') != -1 \
                    or response.find('Мемы') != -1 \
                    or response.find('мемы') != -1 \
                    or response.find('Мемасик') != -1:
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': 'Кто-то сказал MEM?\nНу лови))))',
                                   'random_id': 0,
                                   'attachment': 'photo66105035_' + str(random.choice(pickss))})
        elif event.from_me and not event.from_user:
            if response == "Пошел нахуй" \
                    or response == "Пошел на хуй" \
                    or response == "Пнх":
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': 'Сам иди!',
                                   'random_id': 0})
            elif response == "Люблю тебя":
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': 'А я тебя люблю',
                                   'random_id': 0})
            elif response == "Ику" \
                    or response == "Мой iq" \
                    or response == "iq" or \
                    response == "Iq" or \
                    response == "Айкью":
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': 'Твой iq ' + str(random.choice(iq)),
                                   'random_id': 0})
            elif response.find('Мем') != -1 \
                    or response.find('мем') != -1 \
                    or response.find('Мемы') != -1 \
                    or response.find('мемы') != -1 \
                    or response.find('Мемасик') != -1:
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': '',
                                   'random_id': 0,
                                   'attachment': 'photo66105035_' + str(random.choice(pickss))})

        elif event.from_me and not event.from_chat:
            if response == "Пошел нахуй" \
                    or response == "Пошел на хуй" \
                    or response == "Пнх":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id,
                                   'message': 'Сам иди!',
                                   'random_id': 0})
            elif response == "Люблю тебя":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id,
                                   'message': 'А я тебя люблю',
                                   'random_id': 0})
            elif response == "Ику" \
                    or response == "Мой iq" \
                    or response == "iq" or \
                    response == "Iq" or \
                    response == "Айкью":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id,
                                   'message': 'Твой iq ' + str(random.choice(iq)),
                                   'random_id': 0})
            elif response.find('Мем') != -1 \
                    or response.find('мем') != -1 \
                    or response.find('Мемы') != -1 \
                    or response.find('мемы') != -1 \
                    or response.find('Мемасик') != -1:
                vk_session.method('messages.send',
                                  {'user_id': event.user_id,
                                   'random_id': 0,
                                   "message": '',
                                   'attachment': 'photo66105035_' + str(random.choice(pickss))})

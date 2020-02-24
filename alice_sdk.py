import json
import logging
from typing import List


class AliceResponse:
    def __init__(self, session, version):
        self.__response = {
            'response': {
                'text': '',
                'end_session': False,
            },
            'session': session,
            'version': version
        }
        self.__text_changed = False

    def end(self):
        self.__response['response']['end_session'] = True

    def set_message(self, text: str or None):
        self.__response['response']['text'] = text
        self.__text_changed = True

    def add_message(self, text: str):
        self.__response['response']['text'] += text
        self.__text_changed = True

    def body(self) -> dict:
        if not self.__text_changed:
            logging.warning('Response text has not been changed!')
        return self.__response

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return json.dumps(self.__response)


class AliceRequest:
    def __init__(self, request: str):
        self.__request = json.loads(request)
        self.__entities = self.__get_entities()

    def __get_entities(self) -> dict:
        result = dict()
        for entry in self.__request['request']['nlu']['entities']:
            if entry['type'] == 'YANDEX.FIO':
                result['YANDEX.FIO'] = entry['value']
            elif entry['type'] == 'YANDEX.NUMBER':
                result['YANDEX.NUMBER'] = entry['value']
        return result

    @property
    def user_message(self) -> str:
        return self.__request['request']['command']

    @property
    def number(self) -> str or None:
        return self.__entities.get('YANDEX.NUMBER')

    @property
    def fio(self) -> str or None:
        return self.__entities.get('YANDEX.FIO')

    @property
    def tokens(self) -> List[str]:
        return self.__request['request']['nlu']['tokens']

    @property
    def is_new_user(self) -> bool:
        return self.__request['session']['new']

    def create_response(self) -> AliceResponse:
        return AliceResponse(self.__request['session'], self.__request['version'])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return json.dumps(self.__request)

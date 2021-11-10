import json


class ColorizeMixin:
    repr_color_code = 32

    def __repr__(self):
        format_code = f'\033[0;{self.repr_color_code};1m'
        return format_code


class Advert(ColorizeMixin):

    def __init__(self, json_dict):
        self.price = 0
        for key in json_dict.keys():
            if isinstance(json_dict[key], dict):
                self.__dict__[key] = Advert(json_dict[key])
            else:
                self.__dict__[key] = json_dict[key]
        if self.price < 0:
            raise ValueError('must be >= 0')

    def __repr__(self):
        return super().__repr__() + f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{ 
                    "title": "python", 
                    "price": 1, 
                    "location": { 
                        "address": "город Москва, Лесная, 7", 
                        "metro_stations": ["Белорусская"] 
                        }
                    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad)

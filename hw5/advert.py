import json
import keyword


class ColorizeMixin:
    repr_color_code = 32

    def __repr__(self):
        text = super().__repr__()
        return f'\033[0;{self.repr_color_code};1m{text}'


class BaseAdvert:
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class JsonObject:
    def __init__(self, json_dict):
        for key, value in json_dict.items():
            if isinstance(value, dict):
                value = JsonObject(value)
            if key in keyword.kwlist:
                setattr(self, f'{key}_', value)
            else:
                setattr(self, key, value)


class Advert(ColorizeMixin, JsonObject, BaseAdvert):
    def __init__(self, json_dict):
        super().__init__(json_dict)
        if 'title' not in json_dict.keys():
            raise AttributeError('title does not exists')
        if 'price' not in json_dict.keys():
            setattr(self, 'price', 0)

    @property
    def price(self):
        return self.price_

    @price.setter
    def price(self, val):
        if val < 0:
            raise ValueError('must be >= 0')
        self.price_ = val


if __name__ == '__main__':
    lesson_str = """{ 
                    "title": "python",
                    "price": 1,
                    "location": { 
                        "address": "город Москва, Лесная, 7", 
                        "metro_stations": ["Белорусская"] 
                        },
                    "class": "dog"
                    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad.price)
    print(lesson_ad.class_)
    print(lesson_ad)

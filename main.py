def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print(
        'Утка-маляр взяла зонтик. \n'
        'Однако она не учла, что зонт - это все-таки оружие и надо соблюдать правила безопасности. \n'
        'Бармен решил, что утка, взявшая зонтик, - ненормальная, и попросил ее уйти. \n'
        'Утка же заявила, что не выйдет из-под зонтика, пока бармен не исполнит ее желание.'
    )

def step2_no_umbrella():
    print(
        'Утка-маляр не взяла зонтик. \n'
        'На улице шел ливень. \n'
        'Она долго смотрела на вывески, раздумывая, как бы ей укрыться от дождя. \n'
        'Наконец она подошла к магазину с зонтиками и сказала: \n'
        '— Этот зонт мне подходит! \n'
        'Продавец ответил: \n'
        '— Я рад, что смог угодить Вам.'
    )

if __name__ == '__main__':
    step1()
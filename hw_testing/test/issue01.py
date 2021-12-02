from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе
    >>> str(encode('SOS'))
    '... --- ...'
    >>> str(encode('SOS')) #doctest: +ELLIPSIS
    '... ... ...'
    >>> str(encode('{'))
    Traceback (most recent call last):
    KeyError: '{'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)

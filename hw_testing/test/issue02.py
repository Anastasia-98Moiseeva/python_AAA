from morse import decode
import pytest


@pytest.mark.parametrize('msg, expected',
                         [('... --- ...', 'SOS'), ('. . .', 'EEE'), ('...-- -.... ----.', '369')])
def test_decode(msg, expected):
    assert decode(msg) == expected

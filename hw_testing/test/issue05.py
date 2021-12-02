from what_is_year_now import what_is_year_now
from unittest.mock import patch
import io
import pytest


class TestWhatIsYearNow:
    @patch('urllib.request.urlopen', io.StringIO)
    def test_ymd_sep(self):
        json_data = '{"currentDateTime": "2021-12-11 10:05:43"}'
        with patch('what_is_year_now.API_URL', json_data):
            year = what_is_year_now()

        assert year == 2021

    @patch('urllib.request.urlopen', io.StringIO)
    def test_dmy_sep(self):
        json_data = '{"currentDateTime": "11.12.2021 10:05:43"}'
        with patch('what_is_year_now.API_URL', json_data):
            year = what_is_year_now()

        assert year == 2021

    @patch('urllib.request.urlopen', io.StringIO)
    def test_unknown_year(self):
        json_data = '{"currentDateTime": "11.12.21 10:05:43"}'
        with patch('what_is_year_now.API_URL', json_data):
            with pytest.raises(ValueError):
                what_is_year_now()

    @patch('urllib.request.urlopen', io.StringIO)
    def test_unknown_separator(self):
        json_data = '{"currentDateTime": "11:12:2021 10:05:43"}'
        with patch('what_is_year_now.API_URL', json_data):
            with pytest.raises(ValueError):
                what_is_year_now()

    @patch('urllib.request.urlopen', io.StringIO)
    def test_unknown_key(self):
        json_data = '{"date": "11:12:2021 10:05:43"}'
        with patch('what_is_year_now.API_URL', json_data):
            with pytest.raises(KeyError):
                what_is_year_now()

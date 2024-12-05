import pytest


@pytest.fixture
def numbers_16():
    return "7000792289606361"


@pytest.fixture
def numbers_16_spases():
    return "7000 7922 8960 6361"


@pytest.fixture
def numbers_16_int():
    return 7000792289606361


@pytest.fixture
def numbers_20():
    return "70007922896063611234"


@pytest.fixture
def numbers_20_spases():
    return "70007 92289 60636 11234"


@pytest.fixture
def numbers_20_int():
    return 70007922896063611234


@pytest.fixture
def numbers_19():
    return "7000792289606361123"


@pytest.fixture
def numbers_21():
    return "700079228960636112345"


@pytest.fixture
def numbers_13():
    return "7000792289606"


@pytest.fixture
def numbers_12():
    return "700079228960"


@pytest.fixture
def letters():
    return "тестовые_буквы"


@pytest.fixture
def numbers_and_letters():
    return "a1b2c3d4e5f6g7h8i9j0"


@pytest.fixture
def blank():
    return ""


@pytest.fixture
def test_dict_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def test_dict_list_incorrect_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '12/09/2017 21;42'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'четырнадцатое октября две тысячи восемнадцатого года'}]


@pytest.fixture
def test_dict_list_incorrect_date_second_version():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'четырнадцатое октября две тысячи восемнадцатого года'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '12/09/2017 21;42'}]

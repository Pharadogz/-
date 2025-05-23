import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default_value(test_dict_list):
    assert filter_by_state(test_dict_list) == [
        {"id": 41428829, "state": "EXECUTED",
         "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state(test_dict_list):
    assert filter_by_state(test_dict_list, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED",
         "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_without_requested_state(test_dict_list):
    assert filter_by_state(test_dict_list, "AUTHORIZATION") == []


def test_sort_by_date(test_dict_list):
    assert sort_by_date(test_dict_list) == [
        {"id": 41428829, "state": "EXECUTED",
         "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED",
         "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_reverse(test_dict_list):
    assert sort_by_date(test_dict_list, False) == [
        {"id": 939719570, "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED",
         "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED",
         "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_incorrect_formating(test_dict_list_incorrect_date):
    with ((pytest.raises(ValueError))):
        var = sort_by_date(
            test_dict_list_incorrect_date) == ("Invalid microformat string"
                                               ": '30.06.2018'")


def test_sort_by_date_incorrect_formating_texting(
        test_dict_list_incorrect_date_second_version):
    with pytest.raises(ValueError):
        var = sort_by_date(
            test_dict_list_incorrect_date_second_version) == (
            "Invalid isoformat string: 'Четырнадцатое октября две"
            "Тысячи восемнадцатого года'")

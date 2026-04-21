#!/usr/bin/env python3
from typing import Any
from data_processor import NumericProcessor, TextProcessor, LogProcessor
import pytest


@pytest.fixture
def test_numeric_processor():
    return NumericProcessor()


@pytest.fixture
def test_text_processor():
    return TextProcessor()


@pytest.fixture
def test_log_processor():
    return LogProcessor()


def test_numeric_validate(test_numeric_processor):
    test1 = test_numeric_processor.validate([12, 3.8, 11, 191, 191110.1])
    test2 = test_numeric_processor.validate([2, "hello", 11, 191, 191110.1])
    test3 = test_numeric_processor.validate(12)
    test4 = test_numeric_processor.validate(12.1)
    test5 = test_numeric_processor.validate("None")
    assert test1
    assert not test2
    assert test3
    assert test4
    assert not test5


def test_numeric_ingeste():
    pr = NumericProcessor()
    input = [12, 3.8, 11, 191, 191110.1]
    pr.ingest(input)
    assert len(pr.processed_data) == len(input)

    pr = NumericProcessor()
    input = [2, "hello", 11, 191, 191110.1]
    pr.ingest(input)
    assert len(pr.processed_data) == 0

    pr = NumericProcessor()
    input = 12
    pr.ingest(input)
    assert len(pr.processed_data) == 1

    pr = NumericProcessor()
    input = 12.1
    pr.ingest(input)
    assert len(pr.processed_data) == 1

    pr = NumericProcessor()
    input = "None"
    pr.ingest(input)
    assert len(pr.processed_data) == 0


def test_text_validate(test_text_processor):
    pr = test_text_processor
    test1 = pr.validate("valid")
    test2 = pr.validate(["valid", "very valid"])
    test3 = pr.validate(42)
    test4 = pr.validate(["not valid", 42])
    assert test1
    assert test2
    assert not test3
    assert not test4


def test_log_val_dict_true(test_log_processor):
    assert test_log_processor.validate({"hello": "world"})


def test_log_val_dict_false(test_log_processor):
    assert not test_log_processor.validate({1: 1})


def test_log_val_list_dict_true(test_log_processor):
    assert test_log_processor.validate([{"h": "w", "new": "old"}, {"hello": "world"}])


def test_log_val_list_dict_false(test_log_processor):
    assert not test_log_processor.validate([{"h": "w", "new": "old"}, {42: "world"}])


def test_log_val_false(test_log_processor):
    assert not test_log_processor.validate("this is a string")


def test_log_ingest_dict_true(test_log_processor):
    data: Any = {"hello": "world"}
    test_log_processor.ingest(data)
    assert test_log_processor.processed_data == [data]


def test_log_ingest_dict_false(test_log_processor):
    data: Any = {1: 1}
    test_log_processor.ingest(data)
    assert test_log_processor.processed_data == []


def test_log_ingest_list_false(test_log_processor):
    data: Any = [{1: 1}, "true", 42]
    test_log_processor.ingest(data)
    assert test_log_processor.processed_data == []


def test_log_ingest_dict_list_true(test_log_processor):
    data: Any = [{"h": "w", "new": "old"}, {"hello": "world"}]
    test_log_processor.ingest(data)
    assert test_log_processor.processed_data == data

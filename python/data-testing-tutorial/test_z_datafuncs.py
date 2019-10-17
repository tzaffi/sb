import z_datafuncs as dfn

import numpy as np
import pytest
import yaml
import pandas as pd

def empty_np_array():
    return np.array([])

def np_array(*elts):
    return np.array(elts)

def test_increment():
    assert dfn.increment(2) == 3

def test_min_max_scaler():
    x = empty_np_array()
    assert np.allclose(dfn.min_max_scaler(x), empty_np_array())

    actual = dfn.min_max_scaler(np_array(1,2,3))
    expected = np_array(0, 0.5, 1)
    assert isinstance(actual, np.ndarray), "x should be a numpy array"
    assert np.allclose(actual, expected)

    actual = dfn.min_max_scaler(np_array(10,10,10))
    expected = 0.5
    assert np.allclose(actual, expected)

    with pytest.raises(AttributeError):
        dfn.min_max_scaler(2)

def test_strip_punctuation():
    text     = "this is,    a sentence.!!!"
    expected = "this is    a sentence"
    assert dfn.strip_punctuation(text) == expected

    
def test_bag_of_words():
    text = "this is,    a sentence.!!!"
    expected = set(["this", "is", "a",  "sentence"])
    assert dfn.bag_of_words(text) == expected

def test_budget_schemas():
    columns = dfn.read_metadata('data/metadata_budget.yml')['columns']
    df = pd.read_csv('data/boston_budget.csv')

    dfn.check_schema(df, columns)


def test_ei_schemas():
    columns = dfn.read_metadata('data/metadata_ei.yml')['columns']
    df = pd.read_csv('data/boston_ei-corrupt.csv')

    dfn.check_schema(df, columns)


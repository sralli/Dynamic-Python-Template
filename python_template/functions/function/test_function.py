import pytest 
from python_template import function # TO check if automatic import works or not
from python_template import ENV #To check regular imports work or not

def test_function():
    assert "Dummy Function" == function()

def test_env_function():
    assert ENV == "YAY"
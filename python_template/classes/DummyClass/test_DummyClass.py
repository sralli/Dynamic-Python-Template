import pytest
from python_template import DummyClass

def test_init_class():
    assert "Dummy" == DummyClass().dummy_var

def test_dummy_class():
    dc = DummyClass()
    dc.dummy_method()
    assert "Dummy_Var" == dc.dummy_var
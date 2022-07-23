import pytest
from package.api import testfunc

def test_func():
    res = testfunc()
    assert res == "Testing"
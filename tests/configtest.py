import pytest

from package.api import testfunc

@pytest.fixture
def api():
    return testfunc()
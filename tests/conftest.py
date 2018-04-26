import pytest

from keep_current_storage.app import create_app
from keep_current_storage.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)

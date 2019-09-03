import pytest
from api.tests.factories.users import UserFactory
from pytest_factoryboy import register

register(UserFactory, 'user')


@pytest.fixture
def user_qty():
    return 1


@pytest.fixture
def users(user_qty):
    return UserFactory.create_batch(size=user_qty, is_staff=False)

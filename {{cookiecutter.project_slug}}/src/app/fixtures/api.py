import pytest

from app.testing import ApiClient


@pytest.fixture
def as_anon():
    return ApiClient()


@pytest.fixture
def as_user(user):
    return ApiClient(user=user)

import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from main.models import Game, Publisher


@pytest.fixture(scope='function')
def api_client() -> APIClient:
    yield APIClient()

@pytest.fixture(scope='function')
def user() -> User:
    yield User.objects.create_user(username='adminuser', email='adminuser@gmail.com', password='1234')

@pytest.fixture(scope='function')
def other_user() -> User:
    yield User.objects.create_user(username='otheruser', password='1234')

@pytest.fixture(scope='function')
def game(user, publisher) -> Game:
    yield Game.objects.create(owner=user, title='game', description='description', price= 34, publisher=publisher)

@pytest.fixture(scope='function')
def other_user_game(other_user, publisher) -> Game:
    yield Game.objects.create(owner=other_user, title='other game', description='other description', price= 34, publisher=publisher)

@pytest.fixture(scope='function')
def publisher(user):
    yield Publisher.objects.create(name='Test Publisher', owner=user)


import pytest
from django.urls import reverse


#get

@pytest.mark.django_db
def test_get_game_list(api_client, game):
    response = api_client.get('/games/', format='json')
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_game_detail(api_client, game):
    response = api_client.get(f'/games/{game.id}/', format='json')
    assert response.status_code == 200
    assert response.data['title'] == game.title

@pytest.mark.django_db
def test_get_game_empty_list(api_client) -> None:
    response = api_client.get('/games/', format='json')
    assert response.status_code == 200
    assert response.data == []

@pytest.mark.django_db
def test_get_unpublished_game(api_client):
    response = api_client.get('/games/1320/', format='json')
    assert response.status_code == 404


#post

@pytest.mark.django_db
def test_create_game_no_auth(api_client, publisher):
    response = api_client.post('/games/', {'title': 'game', 'description': 'without token', 'publisher': publisher.id}, format='json')
    assert response.status_code == 401

@pytest.mark.django_db
def test_create_game_with_auth(api_client, user, publisher):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {'username': user.username, 'password': '1234'}, format='json').data
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.post('/games/', {'title': "game", 'description': "with token", 'price': 34, 'publisher': publisher.id} , format='json')

    assert response.status_code == 201
    assert response.data['title'] == 'game'
    assert response.data['description'] == 'with token'
    assert response.data['owner'] == user.username

@pytest.mark.django_db
def test_create_game_with_invalid_data(api_client, user, publisher):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {'username': user.username, 'password': '1234'}, format='json').data
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.post('/games/', {'title': '', 'publisher': publisher.id}, format='json')
    assert response.status_code == 400


#put

@pytest.mark.django_db
def test_update_game_owner(api_client, game, user, publisher):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {'username': user.username, 'password': '1234'}, format='json').data
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.put(f'/games/{game.id}/', {'title': 'new title', 'description': 'new description', 'price': 34, 'publisher': publisher.id}, format='json')

    assert response.status_code == 200
    assert response.data['title'] == 'new title'
    assert response.data['description'] == 'new description'

@pytest.mark.django_db
def test_update_game_not_owner(api_client, user, other_user_game):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {'username': user.username, 'password': '1234'}, format='json').data
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.put(f'/games/{other_user_game.id}/', {'title': 'new title', 'description': 'new description', 'price': 34, 'publisher': other_user_game.publisher.id}, format='json')
    assert response.status_code == 403

#delete

@pytest.mark.django_db
def test_delete_game_owner(api_client, user, game):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {'username': user.username, 'password': '1234'}, format='json').data
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.delete(f'/games/{game.id}/', format='json')
    assert response.status_code == 204

@pytest.mark.django_db
def test_delete_game_not_owner(api_client, user, other_user_game):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {'username': user.username, 'password': '1234'}, format='json').data
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.delete(f'/games/{other_user_game.id}/', format='json')
    assert response.status_code == 403

@pytest.mark.django_db
def test_delete_unreal_game(api_client, user):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {'username': user.username, 'password': '1234'}, format='json').data
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.delete(f'/games/1343/', format='json')
    assert response.status_code == 404


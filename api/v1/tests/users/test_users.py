import faker
import pytest


@pytest.mark.django_db
class TestUsers:
    @pytest.mark.parametrize('user__is_staff', [True, False])
    def test_detail(self, client, user, user__is_staff):
        """
        test user details
            * check basic structure
            * check for 2 types of users (staff|usual)
        """
        res = client.get(f'/api/users/{user.id}')
        assert res.status_code == 200
        user_dict = res.json()
        assert user_dict.get('username')
        assert user_dict.get('email')
        assert user_dict.get('url')
        assert user_dict.get('is_staff') is user__is_staff

    @pytest.mark.parametrize('user_qty', [0, 1, 10, 100])
    def test_list(self, client, users, user_qty):
        res = client.get('/api/users')
        assert res.status_code == 200
        assert isinstance(res.json(), list)
        assert len(res.json()) == user_qty

    @pytest.mark.parametrize('user_qty', [0, 10, 100])
    def test_list_pagination(self, client, users, user_qty):
        limit = 5
        res = client.get(f'/api/users?limit={limit}&offset=0')
        assert res.status_code == 200
        res_json = res.json()
        assert isinstance(res_json, dict)
        assert 'results' in res_json
        users = res_json['results']
        if user_qty:
            assert len(users) == 5
        else:
            assert len(users) == 0

    def test_detail_error(self, client):
        """
        test user details for non-existing user
        """
        res = client.get(f'/api/users/{faker.Faker().random_number()}')
        assert res.status_code == 404

import pytest

from rest_framework import status

pytestmark = pytest.mark.django_db


class TestPageApi:

    def test_pages_endpoint(self, client_api, create_page):
        response = client_api.get('/')
        assert response.status_code == status.HTTP_200_OK

        create_page()
        response = client_api.get('/pages/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data.get('results')) == 1

    def test_page_endpoint(self, client_api, create_page, create_textcontent):
        page = create_page()

        response = client_api.get('/pages/{}/'.format(page.pk))
        assert response.status_code == status.HTTP_200_OK
        result = response.data
        assert len(result.get('textcontent')) == 0

        textcontent = create_textcontent()
        textcontent.pages.add(page)
        response = client_api.get('/pages/{}/'.format(page.pk))
        assert response.status_code == status.HTTP_200_OK
        result = response.data
        assert len(result.get('textcontent')) == 1

import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient

from page.models import Page, TextContent


@pytest.fixture
def client_api() -> APIClient:
    return APIClient()


@pytest.fixture
def create_page():
    def _create_page() -> Page:
        return mixer.blend(Page)

    return _create_page


@pytest.fixture
def create_textcontent():
    def _create_textcontent() -> TextContent:
        return mixer.blend(TextContent)

    return _create_textcontent

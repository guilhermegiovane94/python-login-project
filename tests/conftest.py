import json
from pathlib import Path
from typing import Any, Dict

import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def users_data() -> Dict[str, Any]:
    """Carrega a massa de dados do arquivo fixtures/users.json."""
    fixture_path = Path(__file__).resolve().parent.parent / "fixtures" / "users.json"
    with open(fixture_path, encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Instancia a LoginPage e navega até a página de login antes de cada teste."""
    login = LoginPage(page)
    login.visit()
    return login

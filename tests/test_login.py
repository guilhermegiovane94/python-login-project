import re
from typing import Any, Dict

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


class TestLoginScenarios:
    """Suíte de testes de autenticação cobrindo todos os cenários especificados no README."""

    def test_cenario_1_presenca_e_estado_dos_elementos(self, login_page: LoginPage) -> None:
        """Cenário 1: Presença e Estado dos Elementos.

        Valida a integridade da tela de login:
        - Presença (toBeVisible) e estado habilitado (toBeEnabled) dos campos username, password e botão Login.
        """
        # Campo username
        expect(login_page.username_input).to_be_visible()
        expect(login_page.username_input).to_be_enabled()

        # Campo password
        expect(login_page.password_input).to_be_visible()
        expect(login_page.password_input).to_be_enabled()

        # Botão de Login
        expect(login_page.login_button).to_be_visible()
        expect(login_page.login_button).to_be_enabled()

    def test_cenario_2_preenchimento_de_campos(
        self, login_page: LoginPage, users_data: Dict[str, Any]
    ) -> None:
        """Cenário 2: Preenchimento de Campos.

        Testa inputs a partir da fixture JSON:
        - Preenchimento isolado e conjunto, verificando valor atribuído (toHaveValue).
        """
        valid_user = users_data["validUser"]

        # Preenchimento isolado do username
        login_page.fill_username(valid_user["username"])
        expect(login_page.username_input).to_have_value(valid_user["username"])

        # Preenchimento isolado do password
        login_page.fill_password(valid_user["password"])
        expect(login_page.password_input).to_have_value(valid_user["password"])

        # Limpar campos para testar preenchimento conjunto
        login_page.username_input.clear()
        login_page.password_input.clear()
        expect(login_page.username_input).to_have_value("")
        expect(login_page.password_input).to_have_value("")

        # Preenchimento conjunto
        login_page.fill_both(valid_user["username"], valid_user["password"])
        expect(login_page.username_input).to_have_value(valid_user["username"])
        expect(login_page.password_input).to_have_value(valid_user["password"])

    def test_cenario_3_login_com_sucesso(
        self, login_page: LoginPage, users_data: Dict[str, Any]
    ) -> None:
        """Cenário 3: Login com Sucesso.

        Credenciais válidas (tomsmith):
        - Redirecionamento para /secure, URL segura, mensagem .flash.success e texto
          'You logged into a secure area!'.
        """
        valid_user = users_data["validUser"]

        login_page.fill_both(valid_user["username"], valid_user["password"])
        login_page.click_login()

        # Validações de sucesso
        # "URL segura" especificada no README: verifica protocolo HTTPS e caminho /secure
        expect(login_page.page).to_have_url(re.compile(r"https://.*/secure"))
        expect(login_page.success_message).to_be_visible()
        expect(login_page.flash_message).to_contain_text("You logged into a secure area!")

    def test_cenario_4_credenciais_invalidas(
        self, login_page: LoginPage, users_data: Dict[str, Any]
    ) -> None:
        """Cenário 4: Credenciais Inválidas.

        Usuário e senha incorretos:
        - Permanência na rota /login, exibição de alerta de erro e texto 'Your username is invalid!'.
        """
        invalid_user = users_data["invalidUser"]

        login_page.fill_both(invalid_user["username"], invalid_user["password"])
        login_page.click_login()

        # Validações de erro
        expect(login_page.page).to_have_url(re.compile(r".*/login"))
        expect(login_page.error_message).to_be_visible()
        expect(login_page.flash_message).to_contain_text("Your username is invalid!")

    def test_cenario_5_campos_vazios(
        self, login_page: LoginPage, users_data: Dict[str, Any]
    ) -> None:
        """Cenário 5: Campos Vazios.

        Submissão de formulário sem dados:
        - Permanência na rota /login, exibição de alerta de erro e validação do retorno da aplicação.
        """
        empty_user = users_data["emptyUser"]

        login_page.fill_both(empty_user["username"], empty_user["password"])
        login_page.click_login()

        # Validações
        expect(login_page.page).to_have_url(re.compile(r".*/login"))
        expect(login_page.error_message).to_be_visible()
        expect(login_page.flash_message).to_contain_text("Your username is invalid!")

    def test_cenario_6_fluxo_completo_happy_path(
        self, login_page: LoginPage, users_data: Dict[str, Any]
    ) -> None:
        """Cenário 6: Fluxo Completo (Happy Path).

        Jornada completa de autenticação:
        - Presença → Habilitação → Preenchimento → Submit → Redirecionamento e Mensagem de Sucesso.
        """
        valid_user = users_data["validUser"]

        # 1. Presença e Habilitação
        expect(login_page.username_input).to_be_visible()
        expect(login_page.username_input).to_be_enabled()
        expect(login_page.password_input).to_be_visible()
        expect(login_page.password_input).to_be_enabled()
        expect(login_page.login_button).to_be_visible()
        expect(login_page.login_button).to_be_enabled()

        # 2. Preenchimento
        login_page.fill_both(valid_user["username"], valid_user["password"])
        expect(login_page.username_input).to_have_value(valid_user["username"])
        expect(login_page.password_input).to_have_value(valid_user["password"])

        # 3. Submit
        login_page.click_login()

        # 4. Redirecionamento e Mensagem de Sucesso
        expect(login_page.page).to_have_url(re.compile(r".*/secure"))
        expect(login_page.success_message).to_be_visible()
        expect(login_page.flash_message).to_contain_text("You logged into a secure area!")

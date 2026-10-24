from playwright.sync_api import Locator, Page


class LoginPage:
    """Page Object Model para a página de Login do The Internet Herokuapp."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.username_input: Locator = page.locator("#username")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("button[type='submit']")
        self.flash_message: Locator = page.locator("#flash")
        self.success_message: Locator = page.locator(".flash.success")
        self.error_message: Locator = page.locator(".flash.error")

    def visit(self, url: str | None = None) -> None:
        """Navega para a URL da página de login."""
        self.page.goto(url or self.URL)

    def fill_username(self, username: str) -> None:
        """Preenche o campo de nome de usuário."""
        self.username_input.fill(username)

    def fill_password(self, password: str) -> None:
        """Preenche o campo de senha."""
        self.password_input.fill(password)

    def fill_both(self, username: str, password: str) -> None:
        """Preenche os campos de usuário e senha."""
        self.fill_username(username)
        self.fill_password(password)

    # Alias camelCase para compatibilidade com o padrão original do JS
    fillBoth = fill_both

    def click_login(self) -> None:
        """Clica no botão de submissão do formulário."""
        self.login_button.click()

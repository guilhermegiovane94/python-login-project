# python-login-project

# 🔐 Automação de Login com Playwright, Page Object Model e Fixtures JSON (Python)

> Projeto de automação de testes End-to-End (E2E) para fluxo de autenticação web utilizando **Playwright + Python**, estruturado com o padrão **Page Object Model (POM)**, massa de dados externa (**Fixtures JSON**) e asserções reativas (**Web-First Assertions**).

A aplicação sob teste é o ambiente público de demonstração [The Internet Herokuapp](https://the-internet.herokuapp.com/login).

---

## 📑 Sumário

- [🎯 Objetivo](#-objetivo)
- [✨ Funcionalidades e Cenários](#-funcionalidades-e-cenários)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🛠️ Tecnologias e Boas Práticas](#️-tecnologias-e-boas-práticas)
- [📋 Pré-requisitos](#-pré-requisitos)
- [🚀 Como Executar](#-como-executar)
- [📦 Massa de Dados (Fixtures)](#-massa-de-dados-fixtures)
- [🔁 Arquitetura Page Object Model (POM)](#-arquitetura-page-object-model-pom)
- [📸 Evidências e Relatórios (Traces, Screenshots e HTML)](#-evidências-e-relatórios)
- [🔗 Integração Contínua (CI/CD)](#-integração-contínua-cicd)
- [🤝 Como Contribuir](#-como-contribuir)
- [📄 Licença](#-licença)
- [👨‍💻 Autor](#-autor)

---

## 🎯 Objetivo

Demonstrar a construção de uma suíte de testes E2E robusta e moderna com **Playwright + Python**, aplicando padrões recomendados pela indústria:

- **Automação orientada a dados (Data-Driven Testing):** Consumo desacoplado de dados via arquivo JSON (`fixtures/users.json`).
- **Page Object Model (POM):** Centralização de seletores e métodos de ação na classe `LoginPage`.
- **Web-First Assertions:** Utilização do `expect(...)` nativo do Playwright com auto-waiting para eliminar intermitências (*flakiness*).
- **Validação de ponta a ponta:** Cobertura desde o estado visual/interativo dos elementos até validação de navegação e respostas textuais do backend.

---

## ✨ Funcionalidades e Cenários

| Cenário | Descrição | Validações Aplicadas |
|---|---|---|
| **1. Presença e Estado dos Elementos** | Valida integridade da tela de login | Presença (`to_be_visible`) e estado habilitado (`to_be_enabled`) dos campos `username`, `password` e botão `Login`. |
| **2. Preenchimento de Campos** | Testa inputs a partir da fixture JSON | Preenchimento isolado e conjunto, verificando valor atribuído (`to_have_value`). |
| **3. Login com Sucesso** | Credenciais válidas (`tomsmith`) | Redirecionamento para `/secure`, URL segura (HTTPS), mensagem `.flash.success` e texto `"You logged into a secure area!"`. |
| **4. Credenciais Inválidas** | Usuário e senha incorretos | Permanência na rota `/login`, exibição de alerta de erro e texto `"Your username is invalid!"`. |
| **5. Campos Vazios** | Submissão de formulário sem dados | Permanência na rota `/login`, exibição de alerta de erro e validação do retorno da aplicação. |
| **6. Fluxo Completo (Happy Path)** | Jornada completa de autenticação | Presença → Habilitação → Preenchimento → Submit → Redirecionamento e Mensagem de Sucesso. |

---
## 📁 Estrutura do Projeto

```text
python-login-project/
|-- .github/
|   `-- workflows/
|       `-- ci.yml               # Pipeline de integracao continua (GitHub Actions)
|-- fixtures/
|   `-- users.json               # Massa de dados de teste (usuarios)
|-- pages/
|   |-- __init__.py              # Exporta a classe LoginPage
|   `-- login_page.py            # Page Object Model da tela de autenticacao
|-- tests/
|   |-- __init__.py
|   |-- conftest.py              # Fixtures globais (users_data, login_page)
|   `-- test_login.py            # Suite de testes automatizados com pytest + Playwright
|-- .gitignore                   # Arquivos e diretorios ignorados pelo Git
|-- LICENSE                      # Licenca do projeto
|-- pytest.ini                   # Configuracoes globais do pytest
|-- requirements.txt             # Dependencias do projeto
`-- README.md                    # Documentacao oficial do projeto
```

---
## 🛠️ Tecnologias e Boas Práticas

- **[Playwright](https://playwright.dev/):** Framework E2E rápido, moderno e confiável para browsers Chromium, Firefox e WebKit.
- **[Python](https://www.python.org/) (3.12+):** Linguagem de programação utilizada para a automação.
- **[pytest](https://docs.pytest.org/):** Framework de testes que executa a suíte de testes.
- **[pytest-playwright](https://pytest-playwright.readthedocs.io/):** Integração entre pytest e Playwright.
- **Page Object Model (POM):** Abstração que encapsula detalhes de implementação da interface, promovendo manutenibilidade e reuso.
- **Playwright Locators:** Elementos dinâmicos (`page.locator()`) que resolvem o DOM em tempo de ação com auto-espera.
- **Web-First Assertions (`expect`):** Verificações reativas que aguardam automaticamente a condição esperada antes de estourar timeout.
- **Fixtures JSON:** Desacoplamento entre lógica de teste e valores de entrada.

---

## 📋 Pré-requisitos

Certifique-se de ter instalado em sua máquina:

- **[Python](https://www.python.org/)** (versão 3.10 ou superior recomendado)
- **[pip](https://pip.pypa.io/)** (geralmente instalado junto ao Python)
- Acesso à internet para download dos navegadores e requisições à aplicação de teste.

---

## 🚀 Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/python-login-project.git
cd python-login-project
```

### 2. Criar e ativar o ambiente virtual (Windows)

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Instalar os navegadores do Playwright

```bash
playwright install chromium
```

### 5. Executar os testes

```bash
# Executa todos os testes (headless, Chromium)
pytest tests/test_login.py -v

# Executa com navegador visível (modo headed)
pytest tests/test_login.py -v --headed

# Executa em um navegador específico
pytest tests/test_login.py -v --browser firefox
pytest tests/test_login.py -v --browser webkit

# Executa apenas testes que correspondam a um nome/cenário
pytest tests/test_login.py -v -k "sucesso"

# Gera relatório HTML
pytest tests/test_login.py --html=report.html
```

---
## 📦 Massa de Dados (Fixtures)

Arquivo: [`fixtures/users.json`](fixtures/users.json)

```json
{
  "validUser": {
    "username": "tomsmith",
    "password": "SuperSecretPassword!"
  },
  "invalidUser": {
    "username": "usuario_invalido",
    "password": "senha_errada"
  },
  "emptyUser": {
    "username": "",
    "password": ""
  }
}
```

| Chave | Username | Password | Finalidade no Teste |
|---|---|---|---|
| `validUser` | `tomsmith` | `SuperSecretPassword!` | Validação de login bem-sucedido e navegação para tela restrita. |
| `invalidUser` | `usuario_invalido` | `senha_errada` | Validação de bloqueio de acesso e exibição de erro. |
| `emptyUser` | `""` | `""` | Validação de submissão sem dados preenchidos. |

---

## 🔁 Arquitetura Page Object Model (POM)

O projeto segue estritamente a separação entre a **interface/ações** e a **especificação dos testes**:

1. **`pages/login_page.py`:**
   - Mapeia elementos como instâncias de `page.locator()` no construtor.
   - Fornece métodos de alto nível para ações do usuário (`visit()`, `fill_username()`, `fill_password()`, `fill_both()`, `click_login()`).
   - Não embute asserções rígidas internamente, garantindo flexibilidade às suítes de teste.

2. **`tests/test_login.py`:**
   - Importa e instancia a `LoginPage` via fixture `login_page` definida em `conftest.py`.
   - Utiliza as asserções reativas do Playwright (`expect(...)`).
   - Evita o vazamento de seletores CSS na camada de testes.

```python
# Exemplo de teste aplicando o padrão
def test_login_com_sucesso_deve_navegar_para_secure(login_page, users_data):
    valid_user = users_data["validUser"]

    login_page.fill_both(valid_user["username"], valid_user["password"])
    login_page.click_login()

    expect(login_page.page).to_have_url(re.compile(r"https://.*/secure"))
    expect(login_page.success_message).to_be_visible()
    expect(login_page.flash_message).to_contain_text("You logged into a secure area!")
```

3. **`tests/conftest.py`:**
   - Fixture `users_data` (escopo `session`): carrega a massa de dados de `fixtures/users.json`.
   - Fixture `login_page`: instancia a `LoginPage` e navega até a página de login antes de cada teste.

---

## 📸 Evidências e Relatórios

O pytest-playwright está configurado via [`pytest.ini`](pytest.ini) para capturar evidências automáticas:

- **Screenshots:** Capturados automaticamente quando um teste falha.
- **Vídeos:** Gravados e mantidos em testes com falha.
- **Traces:** Gravados para depuração aprofundada com timeline, snapshots e rede.
- **Relatório HTML:** Gerado com o plugin `pytest-html` e visualizável no navegador.

> 💡 Os diretórios de relatórios e artefatos são ignorados pelo Git via `.gitignore`.

---

## 🔗 Integração Contínua (CI/CD)

O pipeline em [`.github/workflows/ci.yml`](.github/workflows/ci.yml) é acionado a cada `push` e `pull_request` nas branches principais:

```yaml
name: Playwright Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          playwright install chromium

      - name: Run Playwright tests
        run: pytest tests/test_login.py -v

      - name: Upload test results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: pytest-report
          path: |
            report.html
            test-results/
```

O relatório e as evidências da execução no CI ficam disponíveis para download nos **Artifacts** da Action do GitHub.

---

## 🤝 Como Contribuir

1. Faça um **fork** do repositório.
2. Crie uma branch para sua funcionalidade ou correção:
   ```bash
   git checkout -b feature/minha-melhoria
   ```
3. Commit suas alterações seguindo boas práticas de mensagens:
   ```bash
   git commit -m 'feat: adiciona validacao de logout'
   ```
4. Envie a branch para o repositório remoto:
   ```bash
   git push origin feature/minha-melhoria
   ```
5. Abra um **Pull Request**.

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

## 👨‍💻 Autor

Desenvolvido por **Guilherme Giovane**.

Se este projeto foi útil para seus estudos ou implementações de QA, considere deixar uma ⭐ no repositório!
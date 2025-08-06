# mitmproxy

[![Continuous Integration Status](https://github.com/mitmproxy/mitmproxy/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mitmproxy/mitmproxy/actions?query=branch%3Amain)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a38b0325dfb944839c0c8da354f70b1b)](https://app.codacy.com/gh/mitmproxy/mitmproxy/dashboard)
[![autofix.ci: enabled](https://shields.mitmproxy.org/badge/autofix.ci-yes-success?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjZmZmIiB2aWV3Qm94PSIwIDAgMTI4IDEyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCB0cmFuc2Zvcm09InNjYWxlKDAuMDYxLC0wLjA2MSkgdHJhbnNsYXRlKC0yNTAsLTE3NTApIiBkPSJNMTMyNSAtMzQwcS0xMTUgMCAtMTY0LjUgMzIuNXQtNDkuNSAxMTQuNXEwIDMyIDUgNzAuNXQxMC41IDcyLjV0NS41IDU0djIyMHEtMzQgLTkgLTY5LjUgLTE0dC03MS41IC01cS0xMzYgMCAtMjUxLjUgNjJ0LTE5MSAxNjl0LTkyLjUgMjQxcS05MCAxMjAgLTkwIDI2NnEwIDEwOCA0OC41IDIwMC41dDEzMiAxNTUuNXQxODguNSA4MXExNSA5OSAxMDAuNSAxODAuNXQyMTcgMTMwLjV0MjgyLjUgNDlxMTM2IDAgMjU2LjUgLTQ2IHQyMDkgLTEyNy41dDEyOC41IC0xODkuNXExNDkgLTgyIDIyNyAtMjEzLjV0NzggLTI5OS41cTAgLTEzNiAtNTggLTI0NnQtMTY1LjUgLTE4NC41dC0yNTYuNSAtMTAzLjVsLTI0MyAtMzAwdi01MnEwIC0yNyAzLjUgLTU2LjV0Ni41IC01Ny41dDMgLTUycTAgLTg1IC00MS41IC0xMTguNXQtMTU3LjUgLTMzLjV6TTEzMjUgLTI2MHE3NyAwIDk4IDE0LjV0MjEgNTcuNXEwIDI5IC0zIDY4dC02LjUgNzN0LTMuNSA0OHY2NGwyMDcgMjQ5IHEtMzEgMCAtNjAgNS41dC01NCAxMi41bC0xMDQgLTEyM3EtMSAzNCAtMiA2My41dC0xIDU0LjVxMCA2OSA5IDEyM2wzMSAyMDBsLTExNSAtMjhsLTQ2IC0yNzFsLTIwNSAyMjZxLTE5IC0xNSAtNDMgLTI4LjV0LTU1IC0yNi41bDIxOSAtMjQydi0yNzZxMCAtMjAgLTUuNSAtNjB0LTEwLjUgLTc5dC01IC01OHEwIC00MCAzMCAtNTMuNXQxMDQgLTEzLjV6TTEyNjIgNjE2cS0xMTkgMCAtMjI5LjUgMzQuNXQtMTkzLjUgOTYuNWw0OCA2NCBxNzMgLTU1IDE3MC41IC04NXQyMDQuNSAtMzBxMTM3IDAgMjQ5IDQ1LjV0MTc5IDEyMXQ2NyAxNjUuNWg4MHEwIC0xMTQgLTc3LjUgLTIwNy41dC0yMDggLTE0OXQtMjg5LjUgLTU1LjV6TTgwMyA1OTVxODAgMCAxNDkgMjkuNXQxMDggNzIuNWwyMjEgLTY3bDMwOSA4NnE0NyAtMzIgMTA0LjUgLTUwdDExNy41IC0xOHE5MSAwIDE2NSAzOHQxMTguNSAxMDMuNXQ0NC41IDE0Ni41cTAgNzYgLTM0LjUgMTQ5dC05NS41IDEzNHQtMTQzIDk5IHEtMzcgMTA3IC0xMTUuNSAxODMuNXQtMTg2IDExNy41dC0yMzAuNSA0MXEtMTAzIDAgLTE5Ny41IC0yNnQtMTY5IC03Mi41dC0xMTcuNSAtMTA4dC00MyAtMTMxLjVxMCAtMzQgMTQuNSAtNjIuNXQ0MC41IC01MC41bC01NSAtNTlxLTM0IDI5IC01NCA2NS41dC0yNSA4MS41cS04MSAtMTggLTE0NSAtNzB0LTEwMSAtMTI1LjV0LTM3IC0xNTguNXEwIC0xMDIgNDguNSAtMTgwLjV0MTI5LjUgLTEyM3QxNzkgLTQ0LjV6Ii8+PC9zdmc+)](https://autofix.ci)
[![Coverage Status](https://shields.mitmproxy.org/codecov/c/github/mitmproxy/mitmproxy/main.svg?label=codecov)](https://codecov.io/gh/mitmproxy/mitmproxy)
[![Latest Version](https://shields.mitmproxy.org/pypi/v/mitmproxy.svg)](https://pypi.python.org/pypi/mitmproxy)
[![Supported Python versions](https://shields.mitmproxy.org/pypi/pyversions/mitmproxy.svg)](https://pypi.python.org/pypi/mitmproxy)

``mitmproxy`` is an interactive, SSL/TLS-capable intercepting proxy with a console
interface for HTTP/1, HTTP/2, and WebSockets.

``mitmdump`` is the command-line version of mitmproxy. Think tcpdump for HTTP.

``mitmweb`` is a web-based interface for mitmproxy.

## Installation

The installation instructions are [here](https://docs.mitmproxy.org/stable/overview-installation).
If you want to install from source, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Documentation & Help

General information, tutorials, and precompiled binaries can be found on the mitmproxy website.

[![mitmproxy.org](https://shields.mitmproxy.org/badge/https%3A%2F%2F-mitmproxy.org-blue.svg)](https://mitmproxy.org/)

The documentation for mitmproxy is available on our website:

[![mitmproxy documentation stable](https://shields.mitmproxy.org/badge/docs-stable-brightgreen.svg)](https://docs.mitmproxy.org/stable/)
[![mitmproxy documentation dev](https://shields.mitmproxy.org/badge/docs-dev-brightgreen.svg)](https://docs.mitmproxy.org/dev/)

If you have questions on how to use mitmproxy, please
use GitHub Discussions!

[![mitmproxy discussions](https://shields.mitmproxy.org/badge/help-github%20discussions-orange.svg)](https://github.com/mitmproxy/mitmproxy/discussions)

## Contributing

As an open source project, mitmproxy welcomes contributions of all forms.

[![Dev Guide](https://shields.mitmproxy.org/badge/dev_docs-CONTRIBUTING.md-blue)](./CONTRIBUTING.md)

--- 
--- 
---
 
# Análise completa

Segue o resumo dos pontos mais importantes dos relatórios Bandit, focando nos objetivos do trabalho:

### 1. Componentes com Vulnerabilidades Conhecidas

* **Arquivo:** `ASWBXML.py`

* **Trechos avaliados:**
    ```python
    Linha 30: import xml.dom.minidom
    Linha 819: self.xmlDoc = xml.dom.minidom.parseString(strXML)
    ```

* **Vulnerabilidade:**
    O uso de `xml.dom.minidom` para processar XML não confiável pode permitir ataques como XXE (XML External Entity) e outros, pois não há proteção contra conteúdo malicioso.

* **Recomendação:**
    > Utilize a biblioteca `defusedxml` para processar XML de fontes externas, pois ela foi projetada para evitar ataques desse tipo.

### 2. Desserialização Insegura

* **Arquivo:** `magisk.py`

* **Trecho avaliado:**
    ```python
    Linha 90: full_hash = hashlib.md5(ca.subject.public_bytes()).digest()
    ```

* **Vulnerabilidade:**
    O uso do algoritmo MD5 para hash é considerado inseguro, pois é suscetível a colisões e ataques de força bruta.

* **Recomendação:**
    > Substitua MD5 por algoritmos mais seguros, como SHA-256, principalmente para operações relacionadas à segurança.

### 3. Injeção de Comandos

* **Arquivo:** `browser.py`

* **Trechos avaliados:**
    ```python
    Linha 3: import subprocess
    Linha 23: subprocess.run([...])
    Linha 84: subprocess.Popen([...])
    ```

* **Vulnerabilidade:**
    O uso de subprocessos sem validação adequada pode permitir a execução de comandos maliciosos, caso dados externos sejam utilizados.

* **Recomendação:**
    > Sempre sanitize e valide entradas antes de executar comandos do sistema. Evite construir comandos dinamicamente com dados do usuário.

### 4. Validação de Entrada Insuficiente

* **Arquivo:** `emoji.py`

* **Trecho avaliado:**
    ```python
    Linha 1870: r = requests.get("[https://api.github.com/emojis](https://api.github.com/emojis)")
    ```

* **Vulnerabilidade:**
    A ausência de timeout em requisições HTTP pode causar travamentos ou negação de serviço, caso o servidor não responda.

* **Recomendação:**
    > Sempre defina um timeout nas requisições externas e valide as respostas recebidas.

---

## Resumo Final

Os relatórios Bandit mostram que o projeto mitmproxy possui exemplos reais de vulnerabilidades clássicas em código Python, como uso de componentes inseguros, algoritmos de hash quebrados, execução de comandos sem validação e falta de validação de entrada. Essas falhas podem ser exploradas por atacantes e comprometem a segurança do sistema.

Para mitigar esses riscos, recomenda-se:

* Utilizar bibliotecas seguras e atualizadas.
* Adotar algoritmos de hash robustos.
* Validar e sanitizar todas as entradas externas.
* Definir timeouts e tratar exceções em operações de rede.

Essas práticas estão alinhadas com a norma ISO/IEC 27002 e são essenciais para garantir a segurança de aplicações Python em ambientes críticos.

---

## Comandos para rodar o Bandit nos trechos citados

Para executar o Bandit e analisar os principais pontos de vulnerabilidade do projeto, utilize os comandos abaixo no terminal:

```bash
# 1. Componentes com Vulnerabilidades Conhecidas
bandit -r mitmproxy/contrib/wbxml/ASWBXML.py --format txt

# 2. Desserialização Insegura
bandit -r mitmproxy/utils/magisk.py --format txt

# 3. Injeção de Comandos
bandit -r mitmproxy/addons/browser.py --format txt

# 4. Validação de Entrada Insuficiente
bandit -r mitmproxy/utils/emoji.py --format txt
```

Esses comandos irão gerar relatórios detalhados sobre cada vulnerabilidade específica, facilitando a análise e documentação dos riscos encontrados.
import subprocess
import datetime


# Caminho correto para rodar o Bandit em todo o projeto mitmproxy
ALVOS = [
    "mitmproxy/",
]

RELATORIO = "relatorio_bandit.md"

cabecalho = f"""# Relatório de Análise de Segurança com Bandit

**Data da análise:** {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}
**Arquivos analisados:** {', '.join(ALVOS)}

---
"""

def rodar_bandit(alvo):
    resultado = subprocess.run([
        "bandit", "-r", alvo, "--severity", "low", "--format", "txt"
    ], capture_output=True, text=True)
    return resultado.stdout

def gerar_relatorio():
    with open(RELATORIO, "w", encoding="utf-8") as f:
        f.write(cabecalho)
        for alvo in ALVOS:
            f.write(f"\n## Resultado para `{alvo}`\n\n")
            resultado = rodar_bandit(alvo)
            f.write(resultado)
            f.write("\n---\n")
    print(f"Relatório gerado em {RELATORIO}")

if __name__ == "__main__":
    gerar_relatorio()

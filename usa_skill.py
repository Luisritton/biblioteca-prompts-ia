from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()


def carregar(caminho):
    """Lê um arquivo de texto e devolve o conteúdo."""
    with open(caminho, encoding="utf-8") as arquivo:
        return arquivo.read()


def main():
    skill = carregar("skills/analise-vaga/SKILL.md")
    perfil = carregar("contexto/perfil-exemplo.txt")
    vaga = carregar("vagas/vaga-exemplo.txt")

    # Dados vão na mensagem; instruções vão no sistema
    conteudo = f"""<perfil>
{perfil}
</perfil>

<vaga>
{vaga}
</vaga>"""

    resposta = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=conteudo,
        config=types.GenerateContentConfig(
            system_instruction=skill,
            max_output_tokens=5000,
        ),
    )

    print("\nAnálise:")
    print(resposta.text)


if __name__ == "__main__":
    main()
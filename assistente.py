import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Lê o arquivo .env e disponibiliza a chave GEMINI_API_KEY
load_dotenv()

# O cliente busca a chave automaticamente no ambiente
client = genai.Client()


def carregar_contexto(caminho):
    """Lê o arquivo de contexto e devolve o texto."""
    with open(caminho, encoding="utf-8") as arquivo:
        return arquivo.read()


def main():
    contexto = carregar_contexto("contexto/perfil-exemplo.txt")
    pergunta = input("Faça sua pergunta: ")

    prompt = f"""<contexto>
{contexto}
</contexto>

<pergunta>
{pergunta}
</pergunta>

Responda usando somente as informações de <contexto>.
Se a resposta não estiver no contexto, diga que não sabe."""

    resposta = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="Você é um assistente de estudo objetivo e educado.",
            max_output_tokens=400,
        ),
    )

    print("\nResposta:")
    print(resposta.text)


if __name__ == "__main__":
    main()
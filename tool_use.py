from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()


def calcular_media(notas: list[float]) -> float:
    """Calcula a média aritmética de uma lista de notas entre 0 e 10.
    Use esta ferramenta sempre que o usuário pedir média, nota final ou desempenho."""
    print(f"  [ferramenta] calcular_media({notas})")
    if not notas:
        return 0.0
    if any(n < 0 or n > 10 for n in notas):
        raise ValueError("As notas devem estar entre 0 e 10.")
    return sum(notas) / len(notas)


def calcular_porcentagem(valor: float, percentual: float) -> float:
    """Calcula quanto é um percentual de um valor.
    Use esta ferramenta quando o usuário pedir porcentagem, desconto ou acréscimo."""
    print(f"  [ferramenta] calcular_porcentagem({valor}, {percentual})")
    return valor * percentual / 100


def main():
    pergunta = input("Faça sua pergunta: ")

    resposta = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=pergunta,
        config=types.GenerateContentConfig(
            system_instruction="Você é um assistente objetivo. Use as ferramentas disponíveis para cálculos.",
            tools=[calcular_media, calcular_porcentagem],
        ),
    )

    print("\nResposta:")
    print(resposta.text)


if __name__ == "__main__":
    main()
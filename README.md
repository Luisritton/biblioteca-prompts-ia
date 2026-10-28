# Biblioteca de Prompts com Contexto

Projeto em Python que responde perguntas usando somente um arquivo de contexto, com a API do Gemini, e reúne prompts reutilizáveis.

## O que o projeto faz
- Lê um arquivo de contexto e responde apenas com base nele.
- Guarda modelos de prompt em `prompts/`, com tags para organizar as partes.

## Tecnologias
- Python
- Google Gemini API (`google-genai`)
- python-dotenv

## Como executar
1. Clone o repositório.
2. Crie um arquivo `.env` na raiz com:
   GEMINI_API_KEY=sua-chave
3. Instale as dependências:
   pip install -r requirements.txt
4. Rode:
   python assistente.py

## Estrutura
- `assistente.py`: programa principal.
- `contexto/`: arquivos de contexto (exemplos fictícios).
- `prompts/`: modelos de prompt reutilizáveis.

## Aprendizados
- Uso de API e chaves seguras com variáveis de ambiente.
- Prompts estruturados com tags e restrições anti-alucinação.
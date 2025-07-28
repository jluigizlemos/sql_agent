

import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

def main():
    """
    Função principal para configurar e executar o agente SQL.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Validação das variáveis de ambiente
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("OPENAI_API_KEY")

    if not db_url:
        print("Erro: A variável de ambiente DATABASE_URL não foi definida.")
        print("Por favor, crie um arquivo .env e defina a URL do seu banco de dados.")
        return

    if not api_key or api_key == "SUA_CHAVE_API_AQUI":
        print("Erro: A variável de ambiente OPENAI_API_KEY não foi definida.")
        print("Por favor, obtenha uma chave de API da OpenAI e defina no arquivo .env.")
        return

    # Conecta ao banco de dados
    try:
        db = SQLDatabase.from_uri(db_url)
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        print("Verifique se o seu servidor de banco de dados está em execução e se a DATABASE_URL está correta.")
        return

    # Inicializa o modelo de linguagem (LLM)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)

    # Configuração para ocultar a cadeia de pensamento
    import logging
    logging.getLogger('langchain').setLevel(logging.ERROR)
    
    # Cria o agente SQL com verbose=False
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=False)

    print("Agente SQL pronto! Faça suas perguntas sobre as vendas de bicicletas.")
    print("Exemplos: 'Quantas bicicletas foram vendidas no total?' ou 'Qual cliente comprou a bicicleta mais cara?'")
    print("Digite 'sair' para terminar.")

    while True:
        try:
            user_input = input("\nComo posso te ajudar? > ")
            if user_input.lower() == 'sair':
                print("Até logo!")
                break
            
            response = agent_executor.invoke(user_input)
            print("\nResposta:", response.get('output', 'Não foi possível obter uma resposta.'))

        except Exception as e:
            print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()


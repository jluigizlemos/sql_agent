# SQL Agent

## Descrição
O SQL Agent é uma aplicação que permite fazer consultas em linguagem natural a um banco de dados PostgreSQL usando inteligência artificial. O agente utiliza o modelo GPT da OpenAI para interpretar perguntas em português e convertê-las em consultas SQL, retornando respostas de forma clara e objetiva.

## Funcionalidades
- Consultas em linguagem natural ao banco de dados
- Interpretação inteligente de perguntas sobre os dados
- Suporte a banco de dados PostgreSQL
- Interface simples via linha de comando

## Requisitos
- Python 3.8 ou superior
- PostgreSQL
- Chave de API da OpenAI

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd Sql_agent
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
   - Renomeie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` e adicione suas credenciais:
     - `DATABASE_URL`: URL de conexão com o banco de dados PostgreSQL
     - `OPENAI_API_KEY`: Sua chave de API da OpenAI

4. Configure o banco de dados:
   - Execute o script SQL fornecido no arquivo `database.sql` para criar as tabelas e inserir dados de exemplo:
```bash
psql -U seu_usuario -d seu_banco -f database.sql
```

## Uso

Execute o aplicativo com o comando:
```bash
python main.py
```

Exemplos de perguntas que você pode fazer:
- "Quantas bicicletas foram vendidas no total?"
- "Qual cliente comprou a bicicleta mais cara?"
- "Quais são as marcas de bicicletas disponíveis?"
- "Quantas bicicletas o cliente João Silva comprou?"

Para sair do aplicativo, digite `sair`.

## Estrutura do Projeto
- `main.py`: Arquivo principal que configura e executa o agente SQL
- `database.sql`: Script SQL para criar as tabelas e inserir dados de exemplo
- `requirements.txt`: Lista de dependências do projeto
- `.env.example`: Modelo para o arquivo de variáveis de ambiente

## Tecnologias Utilizadas
- LangChain: Framework para desenvolvimento de aplicações com LLMs
- OpenAI GPT: Modelo de linguagem para processamento de linguagem natural
- PostgreSQL: Sistema de gerenciamento de banco de dados relacional
- Python: Linguagem de programação

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
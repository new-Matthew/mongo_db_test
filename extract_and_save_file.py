import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

# Verifica se a URI foi carregada
if uri is None:
    print("Erro: A variável de ambiente MONGODB_URI não foi encontrada.")
else:
    # Cria uma conexão com o MongoDB Atlas
    client = MongoClient(uri)

    try:
        # Acessa uma base de dados (exemplo: 'admin') para testar a conexão
        db = client.admin

        # O comando ismaster é uma forma de checar a conexão
        server_info = db.command("ismaster")

        print("Conexão com o MongoDB Atlas estabelecida com sucesso!")

        # Aqui você pode começar a usar o seu cliente
        # db = client.seu_banco_de_dados
        # collection = db.sua_colecao

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB Atlas: {e}")

    finally:
        # Feche a conexão quando não precisar mais dela
        client.close()

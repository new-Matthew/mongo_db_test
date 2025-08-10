import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

if uri is None:
    print("Erro: A variável de ambiente MONGODB_URI não foi encontrada.")
else:

    client = MongoClient(uri)

    try:

        db = client["db_products"]
        collection = db["products"]
        client.list_database_names()


        server_info = db.command("ismaster")

        print("Conexão com o MongoDB Atlas estabelecida com sucesso!")
        product = {"product": "computer", "amount": 77}
        # 1. Armazena o resultado da inserção em uma variável
        insert_result = collection.insert_one(product)

        # 2. Usa a variável para acessar a ID do documento inserido
        inserted_id = insert_result.inserted_id

        print(f"Documento inserido com sucesso! ID: {inserted_id}")

        # 3. Usa a ID correta para buscar o documento
        inserted_product = collection.find_one({"_id": inserted_id})

        print("\nDocumento encontrado no banco de dados:")
        print(inserted_product)
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB Atlas: {e}")

    finally:
        client.close()

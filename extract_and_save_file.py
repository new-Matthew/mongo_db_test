import os
import requests
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
        # insert
        # product = {"product": "computer", "amount": 77}
        # insert_result = collection.insert_one(product)
        # inserted_id = insert_result.inserted_id
        # print(f"Documento inserido com sucesso! ID: {inserted_id}")
        #vinserted_product = collection.find_one({"_id": inserted_id})
        #print("\nDocumento encontrado no banco de dados:")
        # print(inserted_product)

        response = requests.get("https://labdados.com/produtos")
        if response.status_code == 200:
            response_json = response.json()
            docs = collection.insert_many(response.json())
            
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB Atlas: {e}")

    finally:
        client.close()



from pymongo import MongoClient

# Conecte-se ao MongoDB
client = MongoClient("mongodb+srv://alextuuin:70A5WzWQPPZk6Y6A@cluster0.jgntkli.mongodb.net/")  # Substitua pela URL do seu MongoDB

# Acesse o banco de dados desejado
db = client["CRUD_Plantoes"]  # Substitua pelo nome do seu banco de dados

# Acesse a coleção desejada
collection = db["plantoes"]  # Substitua pelo nome da sua coleção



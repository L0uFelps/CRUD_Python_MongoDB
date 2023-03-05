from pymongo import MongoClient

#Criando uma conexão com o servidor MongoDB:
client = MongoClient('localhost', 27017)

#Acessando o banco de dados desejado:
db = client['bancoTeste']

#Criando uma coleção Usuarios:
usuarios = db['usuarios']

#Criando Usuário:
def criarUsuario(usuario):
    resultado = usuarios.insert_one(usuario)
    return resultado.inserted_id

#Busque um usuario pelo id:
def buscarUserPorId(id):
    usuario = usuarios.find_one({"_id": id})
    return usuario 

#Busque um usuario pelo nome:
def buscarUserPorNome(nome):
    usuario = usuarios.find_one({"nome": nome})
    return usuario

#Atualize usuario pelo id:
def atualisarUser(id, novosDados):
    resultado = usuarios.update_one({"_id": id}, {'$set': novosDados})
    return resultado.modified_count

def deletarUser(id):
    resultado = usuarios.delete_one({"_id": id})
    return resultado.deleted_count

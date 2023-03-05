from pymongo import MongoClient
from main import *

#Crie uma conexão com o servidor do Mongo:
client = MongoClient('localhost', 27017)

#Acesse o banco de dados desejado:
db = client['bancoTeste']

#Crie uma coleção chamada Usuarios:
usuarios = db["usuarios"]

#Crie um novo usuario:
novoUser = {
    'nome': 'Luis Felipe',
    'email': 'luis.silva@colegiooliveiratelles.online',
    'idade': 25
}

idUser = criarUsuario(novoUser)
print('Usuario criado com sucesso! ID: ', idUser)

#Buscando um usuario por id: 
usuarioPorId = buscarUserPorId(idUser)
print('Usuario encontrado pelo ID!: ', usuarioPorId)

#Buscando um usuario pelo nome: 
usuarioPeloNome = buscarUserPorNome('Luis Felipe')
print('Usuario encontrado pelo nome: ', usuarioPeloNome)

#Atualize um usuario pelo id:
dadosAtualizados = {'idade': 26}
resultAtualizacao = atualisarUser(idUser, dadosAtualizados)
print('Usuario atualizado com sucesso! Resultado: ', dadosAtualizados)
print(usuarioPeloNome)

#Delete um usuario pelo id: 
deletarResult = deletarUser(idUser)
print('Usuario deletado com sucesso! Resultado: ', deletarResult)
print(usuarioPeloNome)
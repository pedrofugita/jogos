# CLASSE
#   CARACTERÍSTICAS
#   MÉTODOS

class Cachorros:
    def __init__(self, nome, cor_pelo, idade, tamanho):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print("au au")
    def correr(self):
        print(f'{self.nome} esta correndo')

# MÉTODO CONSTRUTOR
cachorro1 = Cachorros('Toby', 'marrom', 5, 'grande')
cachorro2 = Cachorros('Stela', 'preta', 1, 'pequeno')

print(cachorro1.nome)
print(cachorro1.idade)

# MUDAR UM VALOR
cachorro1.idade = 8
print(cachorro1.idade)

# MÉTODO
cachorro1.latir()
cachorro1.correr()

print(cachorro2.nome)
print(cachorro2.tamanho)
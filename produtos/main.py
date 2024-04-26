class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}'


if __name__ == "__main__":
    pessoa1 = Pessoa("Augusto", 20, "agst@gmail.com")
    print(pessoa1)

    print(pessoa1.nome)
    print(pessoa1.idade)
    print(pessoa1.email)
"""
Ciência da Computação - 3º Semestre
3. Projeto 1 (POO):
Elabore o enunciado de um problema que será resolvido com POO, herança e classe abstrata.
O projeto deve ter no mínimo:
- Uma superclasse abstrata OK
- Duas subclasses OK
- Atributos de instância e atributos de classe
- Alguns métodos gets, sets e pelo menos seis métodos funcionais 
- Métodos sobrescritos OK
- Métodos de classe
- Métodos concretos e métodos abstratos OK
- Programa principal (método main) criando objetos e usando os métodos das classes.
- Listas
"""
from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def Login(self):
        pass
class Paciente(User):
    def __init__(self,login,senha,nome,endereco=None,exame=[]):
        self.login=login
        self.senha=senha
        self.nome=nome
        self.endereco=endereco
    def __str__(self):
        s=f"Cliente: {self.nome}\nLogin:{self.login}\nEndereço atual: {self.endereco}"
        return s
    def Login(self,login,senha):
        log=False
        if self.login==login:
            if self.senha==senha:
                log=True
            else:
                log=False
        else:
            log=False
        if log==True:
            print("\nLogin realizado com sucesso\n")
            return True
        else:
            print("\nDado Inválido, tente novamente\n")
            return False
    def get_nome(self):
        return self.nome
    def get_endereco(self):
        return self.endereco
    def set_endereco(self,new):
        self.endereco = new
    def set_nome(self,new):
        self.nome = new
    def ver_exame(self):
        ...
class Medico(User):
    def __init__(self,login,senha,nome):
        self.login=login
        self.senha=senha
        self.nome=nome
    def Login(self,login,senha):
        log=False
        if self.login==login and self.senha==senha:
            log=True
        else:
            log=False
        if log==True:
            print("\nLogin realizado com sucesso\n")
            return True
        else:
            print("\nDado Inválido, tente novamente\n")
            return False
if __name__ == "__main__":
    #Login do CLIENTE é o CPF
    #Login do MEDICO é o CRM
    c1=Paciente(12345678912,112233,"João Azevedo","apt 404, Edifício Araucárias, QR410, Brasilia, DF")
    a=input("Login: ")
    b=input("Senha: ")
    Paciente.Login(c1,a,b)
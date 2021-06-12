"""
Ciência da Computação - 3º Semestre

1. Terceira verificação de aprendizagem (projeto).
2. Instruções do desenvolvimento do projeto para avaliação:
- Fazer em grupo de até cinco pessoas, mas a apresentação será individual.
- Prazo: enviar dia 16/06/20 até 16h.
- Apresentação: dia 17/06/20 no Google Meet no horário da aula.
- Coloque o nome de todos os alunos do grupo dentro de cada programa ‘.py’
- Apenas um aluno do grupo deve enviar o projeto pela atividade do Classroom em um arquivo
“.zip” (aluno1_aluno2_aluno3_aluno4.zip) com todos os arquivos desenvolvidos:
Um arquivo projeto1 “.py”; e
Um arquivo projeto2 “.py”.
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
    def __init__(self,login,senha,nome,endereco=None,registros=0):
        self.login=login
        self.senha=senha
        self.nome=nome
        self.exame=list()
        self.endereco=endereco
        self.registros=registros
    def __str__(self):
        s=f"Cliente: {self.nome}\nLogin:{self.login}\nEndereço atual: {self.endereco}"
        return s
    def Login(self):
        tentativa=0
        while tentativa<=3:
            login=str(input("Digite o seu CPF: "))
            if len(login)>11 or len(login)<11 or len(login)==0:
                print("CPF inválido")
                tentativa+=1
                continue
            senha=str(input("Digite a sua senha: "))
            if len(senha)==0:
                print("Senha inválida")
                tentativa+=1
                continue
            if str(self.login)==str(login) and str(self.senha)==str(senha):
                log=True
                print("\nLogin realizado com sucesso\n")
                return log
            else:
                print("\nDado Inválido, tente novamente\n")
                tentativa+=1 
        else:
            print("Número de tentativas excedido, encerrando sessão\n")
            log=False
            return log
    def get_nome(self):
        return self.nome
    def get_endereco(self):
        return self.endereco
    def set_endereco(self,new):
        self.endereco = new
    def get_exame(self):
        return self.exame
    def set_nome(self,new):
        self.nome = new
    def marcar_exame(self):
        print(f"Olá, {self.nome}\nPainel De Marcação de Exame")
        tipo = input("Tipo do Exame: ")
        data = input("\nInsira a data(aaaa-mm-dd): ")
        medico = input("\nInsira o nome Médico: ")
        marcado=[tipo,data,medico]
        self.exame.append(marcado)
        self.registros+=1
    def ver_exame(self):
        i=0
        print(f"Histórico de exames do paciente {self.nome}:")
        while i<self.registros:
            print("\n--------------------------------")
            print(f"Exame nº{i+1}")
            print("Tipo de exame:",self.exame[i][0])
            print("\nData do exame:",self.exame[i][1])
            print("\nMédico responsável pelo exame:",self.exame[i][2])
            print("\n--------------------------------")
            i+=1
        print("\n")
    def cancelar_exame(self):
        Paciente.ver_exame(self)
        op=int(input("Selecione, da lista, o nº do exame que deseja remover:\n"))
        confirm=self.exame[op-1]
        while True:
            confmesg=input(f"Deseja cancelar {confirm}?\n[Y]/[N]\n").upper()
            if confmesg=="Y":
                self.exame.pop(op-1)
                print("Operação concluída")
                break
            elif confmesg=="N":
                print("Operação cancelada")
                break
            else:
                print("Opção inválida")
    def remarcar_exame(self):
        Paciente.ver_exame(self)
        op=int(input("Selecione, da lista, o nº do exame que deseja remarcar:\n"))
        confirm=self.exame[op-1]
        while True:
            confmesg=input(f"Deseja remarcar {confirm}?\n[Y]/[N]\n").upper()
            if confmesg=="Y":
                newDate=input("Digite a nova data(aaaa-mm-dd):\n")
                self.exame[op-1][1]=newDate
                print(self.exame[op-1])
                print("Operação concluída")
                break
            elif confmesg=="N":
                print("Operação cancelada")
                break
            else:
                print("Opção inválida")
class Medico(Paciente):
    def __init__(self,login,senha,nome,especialidade):
        super().__init__(login,senha,nome)
        self.especialidade = especialidade
    def Login(self):
        tentativa=0
        while tentativa<=3:
            login=str(input("Digite o seu CRM: "))
            if len(login)==0:
                print("CRM inválido")
                tentativa+=1
                continue
            senha=str(input("Digite a sua senha: "))
            if len(senha)==0:
                print("Senha inválida")
                tentativa+=1
                continue
            if str(self.login)==str(login) and str(self.senha)==str(senha):
                log=True
                print("\nLogin realizado com sucesso\n")
                return log
            else:
                print("\nDado Inválido, tente novamente\n")
                tentativa+=1 
        else:
            print("Número de tentativas excedido, encerrando sessão\n")
            log=False
            return log
    def get_nome(self):
        return self.nome
    def get_crm(self):
        return self.login
    def num_consultas(self,pac):
        con=Paciente.get_exame(pac)
        search=0
        found=[]
        while True:
            if search in con:
                found=[con[search]]
                con.pop[search]
            else:
                if search==(len(con)+1):
                    break
                else:
                    search+=1
        print(f"Consultas marcadas com o paciente {Paciente.get_nome(pac)}: {search-1}")
        i=0
        while i < len(found):
            print("Tipo de exame:",found[i][0])
            print("\nData do exame:",found[i][1])
            i+=1
if __name__ == "__main__":
    #Login do CLIENTE é o CPF
    #Login do MEDICO é o CRM
    c1=Paciente(12345678912,112233,"João Azevedo","apt 404, Edifício Araucárias, QR410, Brasilia, DF")
    m1=Medico(45678,122456,"Carlos Almeida","Pediatra")
    c1.marcar_exame()
    c1.marcar_exame()
    m1.num_consultas(c1)
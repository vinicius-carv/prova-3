"""
Curso: Ciência da Computação
Semestre: 3º Semestre
Disciplina: Projeto Integrador 3
Alunos: Altair Correia de Azevedo
        Arthur Souza Maciel da Silva
        Felipe Ferreira Lima e Lima
        Gustavo Gomes de Jesus
        Vinícius Alves de Carvalho


                                TERCEIRA VERIFICAÇÃO DE APRENDIZAGEM


PROJETO 1 (POO)

Elabore o enunciado de um problema que será resolvido com POO, herança e classe abstrata.
O projeto deve ter no mínimo:
- Uma superclasse abstrata OK
- Duas subclasses OK
- Atributos de instância e atributos de classe
- Alguns métodos gets, sets e pelo menos seis métodos funcionais OK
- Métodos sobrescritos OK
- Métodos de classe OK
- Métodos concretos e métodos abstratos OK
- Programa principal (método main) criando objetos e usando os métodos das classes. OK
- Listas OK
"""

from abc import ABC, abstractmethod # Importar função abstrata.
import random
class User(ABC): # Classe abstrata.
    @abstractmethod
    def Login(self): #Define o método login.
        pass #A instrução pass permite lidar com a condição sem que o loop seja impactado, todo o código continuará sendo lido a menos que um break ou outra instrução ocorra.

class Paciente(User): #Classe Paciente.
    def __init__(self,login,senha,nome,endereco=None,registros=0): # Método Construtor onde todos atributos da classe são declarados.
        self.login=login #Atributo login.
        self.senha=senha #Atributo senha.
        self.nome=nome #Atributo nome.
        self.exame=list() #Atributo lista exame.
        self.endereco=endereco #Atributo endereço.
        self.registros=registros #Atributo registros.
        self.log=False #Atributo boolenano log definido como falso.

    def __str__(self): # Método sobrescrito.
        s=f"Informações do paciente: {self.nome}\nLogin:{self.login}\nEndereço atual: {self.endereco}" #Define o atributo s com uma mensagem pré definida e recebe os atributos nome, ligin e endereço.
        return s #Retorna o valor dos atributos nome, login e endereço na mensagem do atributo s.

    def Login(self): #Função herdada da classe abstrata User.
        tentativa=0 #Define o contador como zero. OBS.: Errar 3 vezes ou a senha ou o usuário ou ambos retorna para a tela inicial.
        while tentativa<=3: #Define que são permitidas 3 tentativas.
            login=str(input("Digite o seu CPF: ")) #Define a variável login com o CPF digitado.
            if len(login)>11 or len(login)<11 or len(login)==0: #Verifica os tamanhos da string CPF OBS.: 3 len é desnecessário.
                print("CPF inválido") #Imprime a mensagem de CPF inválido.
                tentativa+=1 #Adiciona um ao contador se errar.
                continue #Interrompe o ciclo sem interromper o laço de repetição.
            senha=str(input("Digite a sua senha: ")) #Define a variável senha com a senha digitada.
            if len(senha)==0: #Verifica os parametros da string CPF.
                print("Senha inválida") #Imprime a mensagem de senha inválida.
                tentativa+=1 #Adiciona um ao contador se errar.
                continue #Interrompe o ciclo sem interromper o laço de repetição.
            if str(self.login)==str(login) and str(self.senha)==str(senha): #Verifica se o login e a senha digitadas conferem com a dos pacientes já cadastrados. OBS.: Inicialmente só tem cadastrado o paciente p1 para conferência do funcionamento do código.
                self.log=True #Define como verdadeiro a variável booleana log.
                print("\nLogin realizado com sucesso\n") #Imprime a mensagem de login realizado com sucesso.
                return self.log #Retorna o valor do atributo booleano log.
            else: #Caso algum ou todos os laços if anteriores apresente erro, esse laço else é executado.
                print("\nDado Inválido, tente novamente\n") #Imprime a mensagem de dado inválida.
                tentativa+=1 #Adiciona um ao contador se errar.
        else: #Caso o contador tentativa atinja o valor 3 o laço while é interrompido e é executado esse laço else.
            print("Número de tentativas excedido, encerrando sessão\n") #Imprime mensagem de tentativas excedidas.
            self.log=False #Define o atributo booleano log como falso.
            return self.log #Retorna o valor do atributo log.

    def logout(self): #Define o método logout.
        while self.log==True: #Define que enquanto o atributo log for verdadeiro o laço while não é interrompido.
            op = str(input("Você deseja sair?\n[Y]/[N]\n")).upper() #Define a variável op e caso o parametro digitado esteja em letra minúscula, transforma ela em maíuscula.
            if op=="Y": #Verifica se a variável op está definida como Y.
                print("Logout realizado com sucesso") #Imprime a mensagem de login realizado com sucesso.
                self.log = False #Define como falsa a variável booleana log.
                break #A instrução break interrompe do loop caso a condição op=Y seja atendida.
            elif op=="N": #Caso o laço anterior não seja acionado a execução do programa pula para essa instrução e verifica se o atributo da variável op está definida como N.
                print("Logout cancelado") #Imprime a mensagem de logout cancelado.
                break #A instrução break interrompe do loop caso a condição op=N seja atendida.
            else: #Caso nenhuma das intruções anteriores sejam atendidas, é executado a instrução else.
                print("Opção inválida") #Imprime a mensagem de opção inválida.
        else: #Caso o atributo da variável op não seja digitado com as letras S ou N a instrução else é executada.
            print("Login não realizado") #Imprime a mensagem de login não realizado.

    def get_nome(self): #Define o método que busca e retorna o atributo da variável nome.
        return self.nome #Retorna o atributo da variável nome.

    def get_log(self): #Define o método que busca e retorna a variável log.
        return self.log #Retorna o atributo da variável log.

    def get_endereco(self): #Define o método que busca e retorna a variável endereço.
        return self.endereco #Retorna o atributo da variável endereco.

    def set_endereco(self,new): #Define o método que atribui novo valor a variável endereço.
        self.endereco = new #Define o novo valor a variável endereço.

    def get_exame(self): #Define o método que busca e retorna a variável exame.
        return self.exame #Retorna o atributo da variável exame.

    def get_registro(self): #Define o método que busca e retorna a variável registro.
        return self.registros #Retorna o atributo da variável registros.

    def set_nome(self,new): #Define o método que atribui novo valor a variável nome. 
        self.nome = new #Define o novo valor a variável nome.

    def marcar_exame(self): #Define o método marcar_exame.
        print(f"Olá, {self.nome}\nPainel De Marcação de Exame") #Imprime a mensagem definida mostrando o atributo da variável nome.
        tipo = input("Tipo do Exame: ") #Define o atributo da variável tipo.
        data = input("\nInsira a data(aaaa-mm-dd): ") #Define o atributo da variável data.
        medico = input("\nInsira o nome Médico: ") #Define o atributo da variável medico.
        marcado=[tipo,data,medico] #Define a lista marcado os atributos digitados das variáveis tipo, data e medico.
        self.exame.append(marcado) #Insere na lista marcado os atributos digitados das variáveis tipo, data e medico.
        self.registros+=1 #Adiciona um a variável contador registros.

    def ver_exame(self): #Define o método ver_exame.
        i=0 #Define o contador i e atribui seu valor como zero.
        if len(self.exame)>0: #Cria o laço que verifica o tamanho da variável exame.
            print(f"Histórico de exames do paciente {self.nome}:") #Imprime a mensagem de histórico. 
            while i<self.registros: #Cria o laço que verifica se o contador i é maior que o contador registro.
                print("\n--------------------------------")
                print(f"Exame nº{i+1}")
                print("Tipo de exame:",self.exame[i][0])
                print("\nData do exame:",self.exame[i][1])
                print("\nMédico responsável pelo exame:",self.exame[i][2])
                print("\n--------------------------------")
                i+=1
            print("\n")
        else:
            print("Nenhum exame marcado")

    def cancelar_exame(self): 
        Paciente.ver_exame(self) #Chama o método ver_exame mostrando os dados dos exames marcados para o paceinte escolhido.
        op=int(input("Selecione, da lista, o nº do exame que deseja remover:\n"))
        confirm=self.exame[op-1] #Cria a variável confirm e atribui o valor da variável exame a ela.
        while True:
            confmesg=input(f"Deseja cancelar {confirm}?\n[Y]/[N]\n").upper() #Cria a variável confmesg que recebe a variável confirm e mostra a mensagem de confirmação do exame escolhido.
            if confmesg=="Y":
                self.exame.pop(op-1) #Remove o exame da lista.
                print("Operação concluída")
                break
            elif confmesg=="N":
                print("Operação cancelada")
                break
            else:
                print("Opção inválida")

    def remarcar_exame(self): #6
        Paciente.ver_exame(self) #Chama o método ver_exame mostrando os dados dos exames marcados para o paceinte escolhido.
        op=int(input("Selecione, da lista, o nº do exame que deseja remarcar:\n"))
        confirm=self.exame[op-1] #Cria a variável confirm e atribui o valor da variável exame a ela.
        while True:
            confmesg=input(f"Deseja remarcar {confirm}?\n[Y]/[N]\n").upper() #Cria a variável confmesg que recebe a variável confirm e mostra a mensagem de confirmação do exame escolhido.
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
    def __init__(self,login,senha,nome,especialidade): #Construtor
        super().__init__(login,senha,nome) # Herdando login, senha e nome do construtor da classe PACIENTE
        self.especialidade = especialidade
        self.log=False

    def Login(self): #1
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
                self.log=True
                print("\nLogin realizado com sucesso\n")
                return self.log
            else:
                print("\nDado Inválido, tente novamente\n")
                tentativa+=1 
        else:
            print("Número de tentativas excedido, encerrando sessão\n")
            self.log=False
            return self.log

    def logout(self): #2
        while self.log==True:
            op = str(input("Você deseja sair?\n[Y]/[N]\n")).upper()
            if op=="Y":
                print("Logout realizado com sucesso")
                self.log = False
                break
            elif op=="N":
                print("Logout cancelado")
                break
            else:
                print("Opção inválida")
        else:
            print("Login não realizado")

    def get_nome(self):
        return self.nome

    def get_crm(self):
        return self.login

    def num_consultas(self,pac):
        # O objetivo da função é retornar o número de consultas que um paciente já realizou ou irá realizar com um determinado médico
        print(f"\n{Paciente.get_exame(pac)}\n")
        con=list(Paciente.get_exame(pac)) # Armazena a lista de exames de um paciente em uma variável local
        search=i=0
        for i in range(pac.get_registro()):
            if self.nome in con[i]:
                # [[tipo_consulta1,data1,medico1],[tipo_consulta2,data2,medico2],[tipo_consulta3,data3,medico3]...]
                search+=1
                i+=1
            else:
                continue
        return f"Consultas marcadas com o paciente {Paciente.get_nome(pac)}: {search}"

    def registra_paciente(self):
        while True:
            cpf=int(input("Digite o CPF do paciente:\n"))
            if len(str(cpf))<11 or len(str(cpf))>11 or len(str(cpf))==0:
                print("CPF inválido")
                continue
            name=input("Digite o nome do paciente:\n")
            if len(name)==0:
                print("Nome inválido")
                continue
            end=input("Digite o endereço do paciente:\n")
            if len(end)==0:
                print("Endereço inválido")
                continue
            presenha=[] # Armazena os números randômicos como elementos de uma lista
            for i in range(6):
                if i==6:
                    break
                a=random.randint(0,9) #Sorteia um numero de  0 a 9
                presenha.append(a) #Adiciona a lista presenha
                i+=1
                conversor = [str(presenha) for presenha in presenha] # Converter lista de int para lista str
                converter = "".join(conversor) # Lista de str em uma única str
                senha = int(converter) # Converte a str para int
            print(f"Informe a seguinte senha para o seu paciente e peça-o para guardar-la com segurança\nSenha: {senha}")
            return Paciente(cpf,senha,name,end)

if __name__ == "__main__":
    # Para logar como PACIENTE use o CPF e a SENHA na linha 271
    # Para logar como MÉDICO use o CRM e a SENHA na linha 272
    p1=Paciente(12345678912,112233,"João Azevedo","apt 404, Edifício Araucárias, QR410, Brasilia, DF")
    m1=Medico(45678,122456,"Carlos Almeida","Pediatra")
    while True:#1
        print("Bem-vindo ao sistema do Hospital Público de Brasília\nDigite [0] em qualquer um dos menus para encerrar a sessão\n")#1
        inicio=int(input("Você é um:\n[1] - Paciente\n[2] - Médico\n"))#1
        if inicio==1:#1.1
            login=Paciente.Login(p1)#Chama função login da classe paciente. OBS.: Deve entrar com os dados de login do paciente p1 
            while login==True:
                menu=int(input("Selecione uma das opções:\n[1] - Ver histórico de exames\n[2] - Marcar exame\n[3] - Cancelar exame\n[4] - Remarcar exame\n[0] - Fazer logout\n"))
                if menu==1:
                    p1.ver_exame()
                    continue
                elif menu==2:
                    p1.marcar_exame()
                    continue
                elif menu==3:
                    p1.cancelar_exame()
                    continue
                elif menu==4:
                    p1.remarcar_exame()
                    continue
                elif menu==0:
                    p1.logout()
                    break
                else:
                    print("Opção inválida")
            else:
                continue
        elif inicio==2:
            login=Medico.Login(m1)
            while login==True:
                menu=int(input("Selecione uma das opções:\n[1] - Ver consultas com um determinado paciente\n[2] - Marcar exame\n[3] - Cadastrar paciente\n[0] - Fazer logout\n"))
                if menu==1:
                    print(m1.num_consultas(p1))
                elif menu==2:
                    print(f"Agendando exame para {p1.get_nome()}\n")
                    p1.marcar_exame()
                elif menu==3:
                    c2=m1.registra_paciente()
                elif menu==0:
                    m1.logout()
                    break
                else:
                    print("Opção inválida")
        elif inicio==0:
            print("Sessão encerrada")
            break
        else:
            print("Opção inválida")
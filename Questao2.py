"""
4. Projeto 2 (Python e SQL):
- Crie a base de dados;                     -> OK
- Crie pelo menos uma tabela;               ->OK
- Um menu com as opções de CRUD com a tabela criada;
- Use SQL com parâmetros.
"""
import mysql.connector
from mysql.connector import connect, Error

def cria_conexao():
    conexao = mysql.connector.connect(user='root',
                                      password='SUASENHA',
                                      host='127.0.0.1',
                                      database="db_farmacia")

    print('Conexão:', conexao)
    return conexao
    
def fecha_conexao(con):
    con.close
    print('\nConexão Fechada')

def cria_banco():
    sql = "CREATE DATABASE if not exists db_farmacia"
    cursor.execute(sql)

def cria_table():
    sql = """CREATE TABLE IF NOT EXISTS tb_remedio(
        codigo INT UNIQUE NOT NULL AUTO_INCREMENT,
        nome VARCHAR(25) NOT NULL,
        preco FLOAT NOT NULL,
        descricao VARCHAR(100) NULL,
        prescricao BOOL NOT NULL,
        validade DATE NOT NULL,
        PRIMARY KEY (codigo)
        )"""
    cursor.execute(sql)    

def inserir():
    sql = """
        insert into tb_remedio
        (nome,preco,descricao,prescricao,validade)
        values (%s, %s, %s,%s,%s)"""
    i_remedio = input("Nome do remédio: ")
    i_preco = input("Preço do remédio: ")
    i_desc = input("Descrição do remédio: ")
    i_presc = input("Prescrição do remédio: ")
    i_validade = input("Data de Validade(aaaa-mm-dd): ")
    
    valores = (i_remedio,i_preco,i_desc,i_presc,i_validade)
    cursor.execute(sql, valores)
    conexao.commit()

def mostra_dados():
    sql = ''' select * from tb_remedio '''
    cursor.execute(sql)
    registros = cursor.fetchall()
    print('Medicamentos registrados.')
    for row in registros:
        print('Código: ',row[0])
        print('Nome: ',row[1])
        print('Preço: ',row[2])
        print('Descrição: ',row[3])
        print('Prescrição (0-1): ',row[4])
        print('Data de Valiade: ',row[5])

        print('\n')

def atualiza_dados(cod):
    sql = """
        UPDATE tb_remedio
        SET nome=%s,preco=%s
        WHERE codigo = %s """
    i_remedio = input("Nome do remédio: ")
    i_preco = input("Preço do remédio: ")

    valores = (i_remedio, i_preco, cod)
    cursor.execute(sql,valores)
    conexao.commit()

def apagar_dado(cod):
    sql = '''DELETE FROM tb_remedio WHERE codigo = %s '''
    cursor.execute(sql,(cod,))
    conexao.commit()

if __name__ == "__main__":
    #conexao = mysql.connector.connect(user='root',password='arthur159357',host='127.0.0.1',database="")
    conexao = cria_conexao()
    cursor = conexao.cursor()
    cria_banco()
    cria_table()
    while True:
        print('\n---=---=----=----=----=')
        print('Menu CRUD')
        print('1 - Mostrar remedios do banco de dados.')
        print('2 - Inserir um novo remedio.')
        print('3 - Atualizar o `Nome` ou `Preço` de algum remedio.')
        print('4 - Apagar algum remedio do banco de dados.')
        print('Digite qualquer numero para sair.')
        print('\n---=---=----=----=----=')
        opc = int(input('Insira a opção: '))
        if opc == 1:
            mostra_dados()
        elif opc == 2:
            inserir()
        elif opc == 3:
            cod = int(input('insira o codigo do medicamento: '))
            atualiza_dados(cod)
        elif opc == 4:
            cod = int(input('insira o codigo do medicamento: '))
            apagar_dado(cod)
        else:
            break
    cursor.close()
    fecha_conexao(conexao)
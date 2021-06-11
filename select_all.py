"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

"""

from funcoes import *
try:
    conexao = cria_conexao()
    cursor = conexao.cursor()
    ''' Sintaxe:
        select * from nome_tabela           '''
    sql = ''' select * from tb_empregado    '''
    cursor.execute(sql)
    registros = cursor.fetchall()           # registros é uma lista de tuplas
    print('- List of tuplas:')
    print(registros)                        # Mostra os registros na horizontal
    print('- Tuplas:')
    for row in registros:
        print(row)                          # Mostra os registros na vertical
    print("- Colunas, notação de vetor:")
    for row in registros:
        print("Idt:", row[0])
        print("Name:", row[1])
        print("Data nascimento:", row[2])
        print('Gênero:', row[3])
    print("- Colunas, nome coluna:")
    for idt, nome, dta_nascimento, genero, cod_cargo in registros:
        print("Name:", nome)
        print("Data nascimento:", dta_nascimento)
        print('Gênero:', genero)
        print('Código cargo:', cod_cargo)
    print('Registros na tabela:', cursor.rowcount)
    mostra_registros_empregado(conexao)
except Error as erro:
    print('Erro no select all.\n', erro)
else:
    cursor.close()
    fecha_conexao(conexao)

'''

- Posso usar só algumas colunas:
for row in registros:
    print("Idt:", row[0])
    print("Name:", row[1])
- Preciso usar todas as colunas, senão dá erro:
for idt, nome, preco, dta_validade in registros:
    print("Idt:", idt)
    print("Name:", nome)


'''

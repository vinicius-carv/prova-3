import mysql.connector
def cria_conexao():
    conexao = mysql.connector.connect(user='root', password='16Caduceus', host='127.0.0.1', database='db_loja')
    print("Conexão:",conexao)
    return conexao
def fecha_conexao(db):
    db.close()
    print("Conexão fechada.")
def qtd_registros(db):
    cursor = db.cursor()
    sql=''' select *
            from tb_produto'''
    cursor.execute(sql)
    registros = cursor.fetchall()
    print("Registros na tabela:", cursor.rowcount)
def mostra_registros(db):
    cursor=db.cursor()
    sql="""
        select *
        from tb_produto
        """
    cursor.execute(sql)
    registros = cursor.fetchall()
    print('- Registros:')
    for idt, nome, preco, dta_validade in registros:
        print(f'{idt}, {nome}, {dta_validade}')
    qtd_registros(db)
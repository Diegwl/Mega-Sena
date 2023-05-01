from conectar import conexao, cursor


def inserir_jogos(id, n1, n2, n3, n4, n5, n6):
    jogos = f"""INSERT INTO jogos(id, n1, n2, n3, n4, n5, n6)
    values
    ({id}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6});"""
    cursor.execute(jogos)
    conexao.commit()


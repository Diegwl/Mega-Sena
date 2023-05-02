from conectar import conexao, cursor


def listar_jogos():
    sql = 'SELECT * from jogos'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas


def procurar_jogo(n1, n2, n3, n4, n5, n6):
    duques = 0
    ternos = 0
    quadras = 0
    quinas = 0
    megas = 0
    id_mega = 0
    sql = f"SELECT * from jogos"
    cursor.execute(sql)
    linhas = cursor.fetchall()
    for linha in linhas:
        cont = 0
        for i in range(1, 7):
            print(i, end=": ")
            print(linha[i])
            if linha[i] == n1 or linha[i] == n2 or linha[i] == n3 or linha[i] == n4 or linha[i] == n5 or linha[i] == n6:
                cont += 1
                print("foi")
        if cont == 2:
            duques += 1
        elif cont == 3:
            ternos += 1
        elif cont == 4:
            quadras += 1
        elif cont == 5:
            quinas += 1
        elif cont == 6:
            megas += 1
            id_mega = linha[0]
    return [duques, ternos, quadras, quinas, megas, id_mega]

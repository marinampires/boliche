def calcula(jogada):
    pontuacao = 0
    ponto_anterior = 0
    ponto_mais_que_anterior = 0
    num_jogada = 1

    for ponto in jogada:
        if(ponto == "/"):
            pontuacao += 10 - int(ponto_anterior)
        elif(ponto == "X"):
            num_jogada += 1
            pontuacao += 10
        elif(ponto != "-"):
            pontuacao += int(ponto)
            if(ponto_anterior == "X" or ponto_mais_que_anterior == "X" or ponto_anterior == "/" and jogada and num_jogada < 20):
                pontuacao += int(ponto)
        else:
            ponto = 0
        ponto_mais_que_anterior = ponto_anterior
        ponto_anterior = ponto
        num_jogada += 1
    return pontuacao

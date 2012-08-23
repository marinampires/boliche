def calcula(jogada):
    pontuacao = 0
    ponto_anterior = ''
    ponto_mais_que_anterior = ''
    num_jogada = 1
    valor_jogada = 0
    valor_jogada_anterior = 0

    for ponto in jogada:
        if(ponto == "/"):
            valor_jogada = 10 - int(valor_jogada_anterior)
        elif(ponto == "X"):
            num_jogada += 1
            valor_jogada = 10
        elif(ponto != "-"):
            valor_jogada = int(ponto)
        else:
            valor_jogada = 0

        pontuacao += valor_jogada
        if((ponto_anterior == "X" or ponto_mais_que_anterior == "X" or ponto_anterior == "/") and num_jogada < 20):
            pontuacao += valor_jogada

        ponto_mais_que_anterior = ponto_anterior
        ponto_anterior = ponto
        valor_jogada_anterior = valor_jogada
        num_jogada += 1
    return pontuacao

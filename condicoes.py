#condicional if sem parammetros
if numero_ovelhas >= 120: #expresao de teste
    vai_dormi_e_sonhar() # executa se for verdade a expresao de teste
alimentar_cachorros() #fora do bloco if, sempre feita

#if-else
if se_true:
    if_true
else: #se-senao
    if_false

#if-else aninhados
if tempo_bom:
    if restaurante_legal:
        almocamos()
    else:
        comemos_lanche()
else:
    if ingressos_teatro:
        ir_teatro()
    else:
        ir_shopping()

#if-elif-else verifica mais de uma condicao, para quando a primeira é true
if tempo_bom:
    caminhamos()
elif tiver_ingressos: #caso contrario
    ir_teatro()
elif mesas_restaurante:
    almocamos()
else: #se tudo falhar
    ficamos_emCasa()


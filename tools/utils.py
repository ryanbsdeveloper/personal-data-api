from random import randint, choice

class CNPJ():
    def __init__(self) -> None:
        self.regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def formula(self, resultado_das_contas):
        v = 11 - (resultado_das_contas % 11)
        if v > 9:
            v = 0
        return str(v)

    def novocnpj(self, cnpj):
        mult = []
        cnpj = str(cnpj)
        if len(cnpj) > 13:
            cnpj = cnpj[:12]
        if len(cnpj) == 12:
            i1 = [x for x in range(5, 1, -1)] + [x for x in range(9, 1, -1)]
            for v1, v2 in zip(i1, cnpj):
                mult.append(v1 * int(v2))
            soma = sum(mult)
            p_digito = self.formula(soma)
            return f'{cnpj}{p_digito}'
        if len(cnpj) == 13:
            i2 = [x for x in range(6, 1, -1)] + [x for x in range(9, 1, -1)]
            for v1, v2 in zip(cnpj, i2):
                mult.append(int(v1) * v2)
            soma = sum(mult)
            s_digito = self.formula(soma)
            return f'{cnpj}{s_digito}'
        else:
            return

    def gera(self, pontuação=True):
        primeiro_digitos = randint(00, 99)
        primeiro_bloco = randint(000, 999)
        segundo_bloco = randint(000, 999)
        terceiro_bloco = '0001'

        inicio_cnpj = f'{primeiro_digitos}{primeiro_bloco}{segundo_bloco}{terceiro_bloco}00'

        new_cnpj = self.novocnpj(inicio_cnpj)
        new_cnpj = self.novocnpj(new_cnpj)
        try:
            if len(new_cnpj) < 14:
                new_cnpj = new_cnpj + '0'
        except:
            new_cnpj = str(new_cnpj) + '0'

        if pontuação:
            formatado = f'{new_cnpj[0:2]}.{new_cnpj[2:5]}.{new_cnpj[5:8]}/{new_cnpj[8:12]}-{new_cnpj[12:]}'
            return formatado
        else:
            return new_cnpj


def gerador(mascara=False):
    entrada = randint(100000000, 999999999)
    cpf = str(entrada)

    soma = 0
    for pos, c in enumerate(range(10, 1, -1)):
        soma += int(cpf[pos]) * c

    modulo1 = 11 - (soma % 11)

    if modulo1 > 9:
        cpf += '0'
    else:
        cpf += str(modulo1)

    soma_2 = 0
    for pos, c in enumerate(range(11, 1, -1)):
        soma_2 += int(cpf[pos]) * c

    modulo2 = 11 - (soma_2 % 11)

    if modulo2 > 9:
        cpf += '0'
    else:
        cpf += str(modulo2)

    if mascara:
        cpf_mascara = ''
        for c in range(len(cpf)):
            cpf_mascara += cpf[c]
            if c == 2:
                cpf_mascara += '.'
            if c == 5:
                cpf_mascara += '.'
            if c == 8:
                cpf_mascara += '-'
        return cpf_mascara

    return cpf

def data_nascimento():
    ano = randint(1950, 2003)
    mes = randint(1, 12)
    dia = randint(1, 31)

    if mes < 10:
        mes = f'0{mes}'

    if mes == 2:
        dia = randint(1, 28)
        if dia < 10:
            return f'0{dia}/{mes}/{ano}'

    if mes == 6 or mes == 4 or mes == 9 or mes == 11:
        dia = randint(1, 30)
        if dia < 10:
            return f'0{dia}/{mes}/{ano}'
    if dia < 10:
        return f'0{dia}/{mes}/{ano}'
    else:
        return f'{dia}/{mes}/{ano}'

def tel():
    ddd = ['11', '73', '13', '21','11','12']
    
    return f'+55 {choice(ddd)} 9{randint(0000, 9999)}-{randint(0000,9999)}'

def email(nome:str, sobrenome:str):
    nome, sobrenome = nome.lower().replace(' ',''), sobrenome.lower().replace(' ','')
    dominios = ['gmail', 'outlook', 'hotmail', 'yahoo',]
    alt = ['_', '-','.', 'dev', '&', '', '']
    fatia = ['nome', 'sobrenome', 'nenhum']
    comorbr = ['com', 'com.br']

    fatia_select = choice(fatia)
    if fatia_select == 'nome':
        nome = nome[:2]

    elif fatia_select == 'sobrenome':
        sobrenome = sobrenome[:4:]
    
    return f'{nome}{choice(alt)}{sobrenome}@{choice(dominios)}.{choice(comorbr)}'

    

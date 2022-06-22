from random import randint
from secrets import choice
from time import sleep
import requests
from utils import gerador, CNPJ, data_nascimento, email, tel
from sqlalchemy import create_engine

ceps = ['04890570', '57036750', '13800435', '15612044', '13482440', '13065051', '18066418', '18272544', '02046090', '13274464', '13973017', '08620540', '04152040', '16201338', '13568771', '23587545', '41321240', '08111075', '03917080', '09260820', '41321835', '09330510', '13155040', '11724350', '15046230', '04851809', '13484050', '41320210', '06706070', '41307375', '13432512', '41307275', '23580460',
        '14070230', '04893052', '13150023', '05831055', '04852410', '13179288', '03921060', '13807697', '13425701', '15506714', '11330170', '08320250', '13212860', '01321020', '08391575', '11431485', '11615603', '15070330', '14786542', '12228350', '13423588', '03812200', '09840075', '18190000', '18190000', '04618010', '06112000', '13917208', '06266412', '06130030', '13060376', '17209070', '41307275',
        '04890570', '57036750', '13800435', '15612044', '13482440', '13065051', '18066418', '18272544', '02046090', '13274464', '13973017', '08620540', '04152040', '16201338', '13568771', '23587545', '41321240', '08111075', '03917080', '09260820', '41321835', '09330510', '13155040', '11724350', '15046230', '04851809', '13484050', '41320210', '06706070', '41307375', '13432512', '41307275', '23580460',
        '14070230', '04893052', '13150023', '05831055', '04852410', '13179288', '03921060', '13807697', '13425701', '15506714', '11330170', '08320250', '13212860', '01321020', '08391575', '11431485', '11615603', '15070330', '14786542', '12228350', '13423588', '03812200', '09840075', '18190000', '18190000', '04618010', '06112000', '13917208', '06266412', '06130030', '13060376', '17209070', '41307275',
        '14070230', '13285892', '13150023', '05831055', '04852410', '13179288', '41351400', '13807697', '23587545', '15506714', '11330170', '08320250', '13212860', '01321020', '08391575', '11431485', '23548168', '15070330', '14786542', '41321835', '13423588', '03812200', '09840075', '18190000', '15990842', '04618010', '06112000', '13917208', '41320210', '41307275', '13060376', '17209070', '03243040',
        '23580420', '13285892', '13150023', '05831055', '07031190', '13179288', '03921060', '23580420', '13425701', '15506714', '11330170', '08320250', '13212860', '01321020', '08391575', '23587545', '11615603', '15070330', '23555306', '12228350', '13423588', '03812200', '09840075', '13503210', '15990842', '04618010', '18190000', '13917208', '06266412', '06130030', '13060376', '17209070', '23580450', '04890570', '23555310', '41301010', '15612044', '41307105', '13065051', '18066418', '41321841', '02046090', '41321841', '13973017', '08620540', '04152040', '16201338', '13568771', '06402170', '12220480', '08111075', '03917080', '09260820', '16600035', '09330510', '13155040', '11724350', '15046230', '04851809', '41370075', '18708856', '06706070', '11259339', '13432512', '13042860', '15138328',
        '14070230', '13285892', '13150023', '41342638', '41342794', '13179288', '41342662', '13807697', '13425701']


DATABASE_URL = f"postgresql://ryanl:password@db:5432/fastapi_database"

db = create_engine(DATABASE_URL)

sb = []
ns = []
mulher = []


with open("nomes_homens.txt", 'r') as file2:
    for linha in file2.readlines():
        if linha:
            ns.append(str(linha).replace("\n", ""))

with open('nomes_mulheres.txt', 'r') as file2:
    for linha in file2.readlines():
        if linha:
            mulher.append(str(linha).replace("\n", ""))

with open('sobrenomes.txt', 'r') as file:
    for linha in file.readlines():
        if linha:
            sb.append(str(linha).replace("\n", ""))



for i, nome in enumerate(ns):
    url = requests.get(f'https://viacep.com.br/ws/{ceps[randint(2, 239)]}/json')
    sleep(1)
    dados = url.json()
    try:
        estado = dados['uf']
        if not estado:
            estado = 'n/a'
    except:
        estado = 'n/a'
    try:
        cidade = dados['localidade']
        if not cidade:
            cidade = 'n/a'
    except:
        cidade = 'n/a'
    try:
        bairro = dados['bairro']
        if not bairro:
            bairro = 'n/a'
    except:
        bairro = 'n/a'
    try:
        rua = dados['logradouro']
        if not rua:
            rua = 'n/a'
    except:
        rua = 'n/a'

    sexo = 'Masculino'
    db.execute(f"""INSERT INTO "Dados" (nome, sobrenome, sexo, cpf, cnpj, uf, cidade, bairro, rua, nascimento, cep, telefone, email)
VALUES ('{str(ns[i])}', '{str(sb[i]).replace("'", '`')}', '{(str(sexo))}', '{str(gerador(True))}', '{CNPJ().gera()}', '{estado}', '{cidade}', '{bairro.replace("'", "`")}', '{rua}','{data_nascimento()}', '{choice(ceps)}', '{tel()}', '{email(ns[i], sb[i])}');""")
    sleep(1)
    url = requests.get(f'https://viacep.com.br/ws/{ceps[randint(2, 239)]}/json')
    sleep(1)
    dados = url.json()
    try:
        estado = dados['uf']
        if not estado:
            estado = 'n/a'
    except:
        estado = 'n/a'
    try:
        cidade = dados['localidade']
        if not cidade:
            cidade = 'n/a'
    except:
        cidade = 'n/a'
    try:
        bairro = dados['bairro']
        if not bairro:
            bairro = 'n/a'
    except:
        bairro = 'n/a'
    try:
        rua = dados['logradouro']
        if not rua:
            rua = 'n/a'
    except:
        rua = 'n/a'

    sexo = 'Feminino'
    db.execute(f"""INSERT INTO "Dados" (nome, sobrenome, sexo, cpf, cnpj, uf, cidade, bairro, rua, nascimento, cep, telefone, email)
    VALUES ('{str(mulher[i])}', '{str(sb[i]).replace("'", '`')}', '{(str(sexo))}', '{str(gerador(True))}', '{CNPJ().gera()}', '{estado}', '{cidade}', '{bairro.replace("'", "`")}', '{str(rua)}','{data_nascimento()}', '{choice(ceps)}', '{tel()}', '{email(mulher[i], sb[i])}');""")



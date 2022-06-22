# **Principais tecnologias usadas:**

###### ![tecs](C:\Users\ryanl\Downloads\tecs.png)

## API de dados pessoais 🧍‍♂️🧍‍♀️

API documentada com **Swagger** e de fácil utilização, acesse agora: [clique aqui](https://api-dados-pessoais.herokuapp.com/)

#### Sobre

O microsserviço retorna dados pessoais válidos de 200 pessoas, podendo fazer filtragem se desejável.

Para requisição dos dados da API, o usuário terá que criar um hash de autorização com seu email, e inserir o hash na uri para assim ter autorização.

*Codificação do hash: MD5*

#### Desenvolvimento e Implantação 

***Desenvolvimento*** 

A API feita utilizando o framework **FastApi** está em um container de imagem: python3.9, onde está instalado todas dependências do microsserviço. O banco de dados **postgreSQL** está em outro container de imagem: postgres:alpine. Assim pelo container da API faço a conexão com o banco de dados usando **SQLAlchemy**.



***Implantação***  

O Heroku não permite usarmos um container para nosso banco de dados, porém ele oferecem um serviço: Heroku Postgres*, dando acesso a um banco de dados limitado deles. Assim então para implementação do

microsserviço ,fiz o push do container da API para o Heroku já com o serviço de banco de dados deles configurado na aplicação, Pronto API em produção.



#### Tecnologias usadas 

- Python 3.9
- Framework: FastApi
- Swagger
- PostgreSQL
- SQLAlchemy
- Docker
- Hospedagem: Heroku



#### Código-fonte

**dependências:**

`pip install -r requirements.txt`

**banco de dados:**

Escolha de sua preferencia, configure em src/controllers/database.py

🚨***Script para criação de dados pessoais válidos não esta disponibilizado*** 🚨



### PROJETO PESSOAL
import os

from dotenv import load_dotenv

# A função create_engine é utilizada para criar a conexão com o banco de dados
from sqlalchemy import create_engine

# Daqui que vamos utilizar a classe base de onde todas as nossas models (classes) herdarão
from sqlalchemy.ext.declarative import declarative_base

# Utilizamos sessionmaker para criar a sessão de usuário
from sqlalchemy.orm import sessionmaker

# A função load_dotenv carrega informações de um arquivo .env e cria variáveis de ambiente
load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Utilizamos a connection string na criação da conexão com o banco de dados
# mysql+pymysql             -> A conexão e o driver de conexão
# {db_user}:{db_pass}       -> Significa o usuário e a sua senha
# {db_host}:{db_port}       -> O endereço onde o banco está rodando e a porta
# 20230416_aula05   -> O nome do banco de dados que está sendo feita a conexão
connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# Aqui criamos a conexão com banco de dados. O primeiro argumento é a connection string criada
# e o segundo argumento indica que os comandos SQL gerados serão mostramos no terminal
engine = create_engine(connection_string, echo=True)

# Classe base de onde todas as models serão
Base = declarative_base()
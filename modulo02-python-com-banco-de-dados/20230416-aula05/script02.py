
from database import Base, engine
from models import Usuario

if __name__ == "__main__":

    # Cria as tabelas que serão associadas as models
    Base.metadata.create_all(engine)

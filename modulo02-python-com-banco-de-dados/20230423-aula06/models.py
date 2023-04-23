
# Classe que será herdada nas nossas models
from database import Base

# Tipos das colunas que serão criadas na tabela mapeada
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, func, Table

from sqlalchemy.orm import relationship

postagens_categorias = Table(
    "tb_postagens_categorias", Base.metadata,
    Column("postagem_id", Integer, ForeignKey("tb_postagens.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("tb_categorias.id"), primary_key=True)
)


class Usuario(Base):
    
    # O atributo __tablename__ indica o nome da tabela que será criada
    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)

    # Atributos do tipo relationship fazem a ligação entre os objetos que representam as tabelas que
    # possuem relacionamento. Esse campo não existirá fisicamente no banco de dados

    # Primeiro argumento: Nome da classe relacionada
    # back_populates: Representa o campo de ligação no objeto relacionado
    # uselist: Indicamos se queremos trazer uma lista de objetos relacionados ou não
    perfil = relationship("UsuarioPerfil", back_populates="usuario", uselist=False)

    
    def __repr__(self):
        return f"<Usuario({self.email})>"


class UsuarioPerfil(Base):

    __tablename__ = "tb_usuarios_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(200), nullable=False)
    sexo = Column(String(1), nullable=False)

    usuario = relationship("Usuario", back_populates="perfil", uselist=False)


class Postagem(Base):

    __tablename__ = "tb_postagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios_perfis.id"), nullable=False)
    titulo = Column(String(200), nullable=False)
    corpo = Column(Text, nullable=False)


class Categoria(Base):

    __tablename__ = "tb_categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)


class Comentario(Base):

    __tablename__ = "tb_comentarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios_perfis.id"), nullable=False)
    postagem_id = Column(Integer, ForeignKey("tb_postagens.id"), nullable=False)
    texto = Column(String(200), nullable=False)
    data_hora = Column(DateTime, default=func.now)

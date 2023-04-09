/*

Exercício 03

Normalizar a tb_filmes

*/

 -- Criar a tabela tb_filmes

-- O comando abaixo só é necessário em bases de dados SQLite
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tb_diretores(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_atores(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_filmes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	diretor_id INTEGER NOT NULL,
	nome TEXT NOT NULL,
	ano_de_lancamento INTEGER NOT NULL,
	FOREIGN KEY(diretor_id) REFERENCES tb_diretores(id)
);

CREATE TABLE IF NOT EXISTS tb_atores_filmes(
	ator_id INTEGER NOT NULL,
	filme_id INTEGER NOT NULL,
	PRIMARY KEY(ator_id, filme_id),
	FOREIGN KEY(ator_id) REFERENCES tb_atores(id),
	FOREIGN KEY(filme_id) REFERENCES tb_filmes(id)
);

-- Primeiro exercício de 2FN ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS tb_produtos(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	-- É possível criar uma tabela apenas para categorias
	categoria TEXT NOT NULL,
	preco REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_pedidos(
	id INTEGER,
	produto_id INTEGER NOT NULL,
	quantidade INTEGER NOT NULL,
	PRIMARY KEY(id, produto_id),
	FOREIGN KEY(produto_id) REFERENCES tb_produtos(id)
);

-- Segundo exercício 3FN ----------------------------------------------------------------

CREATE TABLE IF NOT EXISTS tb_alunos(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_disciplinas(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_alunos_disciplinas(
	aluno_id INTEGER NOT NULL,
	disciplina_id INTEGER NOT NULL,
	nota_1 REAL NOT NULL,
	nota_2 REAL NOT NULL,
	nota_3 REAL NOT NULL,
	PRIMARY KEY(aluno_id, disciplina_id),
	FOREIGN KEY(aluno_id) REFERENCES tb_alunos(id),
	FOREIGN KEY(disciplina_id) REFERENCES tb_disciplinas(id)
);


-- Criar a estrutura para o usuário

-- Criar a tabela tb_usuarios

-- Cria a tabela tb_usuarios se ela não existir

/*
 * Criamos a coluna id, do tipo integer, que será uma chave primária
 * e terá auto incremento
 * 
 * O campo id será um tipo integer (numérico), chave primária e auto incremento
 * Os campos email e senha serão do tipo text (string) e não poderão conter
 * valores nulos
 */
CREATE TABLE IF NOT EXISTS tb_usuarios(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	email TEXT NOT NULL,
	senha TEXT NOT NULL
);


-- Inserindo dados da tabela tb_usuarios
INSERT INTO tb_usuarios(email, senha) VALUES ("amanda@email.com", "123456");
INSERT INTO tb_usuarios(email, senha) VALUES ("jose@email.com", "123456");

-- O comando abaixo não irá funcionar
INSERT INTO tb_usuarios(email) VALUES ("joao@email.com");

-- Selecionar os dados da tabela
-- O * retorna todas as colunas da tabela
SELECT * FROM tb_usuarios tu ;

-- Por padrão, o SQLITE não faz a verificação de consistência de chave
-- estrangeira entre tabelas. O comando abaixo habilita essa verificação
PRAGMA foreign_keys = ON;

-- Criação da tabela tb_usuarios_perfis
CREATE TABLE IF NOT EXISTS tb_usuarios_perfis(
	id INTEGER PRIMARY KEY,
	nome TEXT NOT NULL,
	sobrenome TEXT NOT NULL,
	idade INTEGER NULL,
	FOREIGN KEY(id) REFERENCES tb_usuarios(id)
);

/*
 * O comando abaixo não irá funcionar, pois estamos tentando adicionar
 * um valor de ID que não existe na tabela referenciada
 */

INSERT INTO tb_usuarios_perfis(id, nome, sobrenome, idade) VALUES (
	10, "João", "Silva", 30
);

INSERT INTO tb_usuarios_perfis(id, nome, sobrenome, idade) VALUES (
	1, "Amanda", "Silva", 20
);

SELECT * FROM tb_usuarios_perfis;

/*
 * Criação da tabela de postagens
 */

CREATE TABLE IF NOT EXISTS tb_postagens(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	usuario_id INTEGER NOT NULL,
	titulo TEXT NOT NULL,
	corpo TEXT NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES tb_usuarios(id)
);

SELECT * FROM tb_postagens tp ;

INSERT INTO tb_postagens (usuario_id, titulo, corpo) VALUES
	(1, "A linguagem Python", "Python é legal");

INSERT INTO tb_postagens (usuario_id, titulo, corpo) VALUES
	(1, "A linguagem Golang", "Golang é rápida");
	
-- O comando abaixo não irá funcionar, pois não existe um id 10 na tabela de usuário
INSERT INTO tb_postagens (usuario_id, titulo, corpo) VALUES
	(10, "A linguagem Coldfusion", "Coldfusion é bem parecido com html");
	
/*
 * Criação da tabela tb_categorias
 */

CREATE TABLE IF NOT EXISTS tb_categorias(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

/*
 * Em uma relação N:N, precisamos criar uma outra tabela, definida como tabela
 * associativa. Basicamente ela fará a associação entre as tabelas que
 * tem a relação N:N
 * 
 * postagem_id e categoria_id são chaves primárias, ou seja, temos uma chave
 * primária composta na tabela
 * Ao mesmo tempo, cada coluna é uma chave estrangeira das tabelas
 * tb_postagem e tb_categorias, respectivamente.
 */

CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
	postagem_id INTEGER NOT NULL,
	categoria_id INTEGER NOT NULL,
	PRIMARY KEY(postagem_id, categoria_id),
	FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
	FOREIGN KEY(categoria_id) REFERENCES tb_categorias(id)
);

INSERT INTO tb_categorias (nome) VALUES ("TI");
INSERT INTO tb_categorias (nome) VALUES ("Proway");
INSERT INTO tb_categorias (nome) VALUES ("Python");

SELECT * FROM tb_categorias tc ;

INSERT INTO tb_postagens_categorias (postagem_id, categoria_id) VALUES (
	1, 1
);

INSERT INTO tb_postagens_categorias (postagem_id, categoria_id) VALUES (
	1, 2
);

INSERT INTO tb_postagens_categorias (postagem_id, categoria_id) VALUES (
	1, 3
);

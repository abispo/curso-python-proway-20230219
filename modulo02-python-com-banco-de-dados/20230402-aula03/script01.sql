/*
A normalização é um processo importante na criação de bancos de dados. É um processo que ajuda a evitar problemas comuns que
ocorrem quando os dados são armazenados de maneira desorganizada. A normalização ajuda a melhorar a eficiência, reduzir a
redundância de dados, melhorar a integridade dos dados e evitar problemas de inconsistência.

Existem várias formas normais que podem ser aplicadas para normalizar os dados em um banco de dados, mas as três primeiras formas
normais são as mais importantes. A primeira forma normal (1FN) define que cada coluna em uma tabela deve conter apenas valores
atômicos e indivisíveis, ou seja, valores únicos e não compostos. Essa forma normal ajuda a evitar a repetição de informações em
uma mesma coluna, o que pode levar a problemas de redundância e inconsistência de dados.
*/

-- Tabela tb_clientes

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	endereco TEXT NOT NULL,
	telefone TEXT NOT NULL
);

INSERT INTO tb_clientes (nome, endereco, telefone) VALUES
	("João da Silva", "Rua XV de Novembro, 1000, Centro, Blumenau, SC", "47998276512"),
	("Neide Carvalho", "Praça da Liberdade, 12, Liberdade, São Paulo, SP", "11989827651, 11999872341"),
	("Maria Souza", "Rua dos Bandeirantes, 240, Centro, Pomedore, SC", "47994888221");

SELECT * FROM tb_clientes tcpf ;

/*
	Podemos aplicar a Primeira Forma Normal (1FN) na tabela tb_clientes seguindo os seguintes passos:
		- "Quebrar" a informação de endereço em múltiplas colunas (tipo_logradouro, numero, etc)
		- Remover a coluna multivalorada "telefone" para uma nova tabela de telefones (tb_telefones)
*/

-- Alterar o nome da tabela tb_clientes
ALTER TABLE tb_clientes RENAME TO tb_clientes_pre_1fn;

SELECT * FROM tb_clientes_pre_1fn;

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	tipo_logradouro TEXT NOT NULL,
	logradouro TEXT NOT NULL,
	numero TEXT NOT NULL,
	bairro TEXT NOT NULL,
	cidade TEXT NOT NULL,
	estado TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_telefones(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	cliente_id INTEGER NOT NULL,
	telefone TEXT NOT NULL,
	FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);

INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado
) VALUES
	("João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
	("Neide Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP");

SELECT * FROM tb_clientes tc ;

PRAGMA foreign_keys = ON;

INSERT INTO tb_telefones (cliente_id, telefone) VALUES
	(1, "47998276512"),
	(2, "11989827651"),
	(2, "11999872341");

SELECT * FROM tb_telefones;

-- Utilizamos INNER JOIN para mostrar dados de tabelas relacionadas
-- Abaixo mostramos os dados nome e cidade da tb_clientes, e telefone da tb_telefones
SELECT tc.nome, tc.cidade, tt.telefone FROM tb_clientes tc 
INNER JOIN tb_telefones tt
ON tc.id = tt.cliente_id WHERE tc.id = 1;

/*
 * Aplicamos a 1FN na tabela tb_clientes fazendo 2 coisas:
 * "Quebramos" o campo endereço em subcampos
 * O campo multivalorado "telefone" removemos da tabela e o colocamos em outra tabela
 * chamada tb_telefones, que é dependente da tabela tb_clientes (1:N)
 */

/*
A normalização é um processo importante na criação de bancos de dados. É um processo que ajuda a evitar problemas comuns que
ocorrem quando os dados são armazenados de maneira desorganizada. A normalização ajuda a melhorar a eficiência, reduzir a
redundância de dados, melhorar a integridade dos dados e evitar problemas de inconsistência.

Existem várias formas normais que podem ser aplicadas para normalizar os dados em um banco de dados, mas as três primeiras formas
normais são as mais importantes. A primeira forma normal (1FN) define que cada coluna em uma tabela deve conter apenas valores
atômicos e indivisíveis, ou seja, valores únicos e não compostos. Essa forma normal ajuda a evitar a repetição de informações em
uma mesma coluna, o que pode levar a problemas de redundância e inconsistência de dados.
*/

-- Tabela tb_clientes

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	endereco TEXT NOT NULL,
	telefone TEXT NOT NULL
);

INSERT INTO tb_clientes (nome, endereco, telefone) VALUES
	("João da Silva", "Rua XV de Novembro, 1000, Centro, Blumenau, SC", "47998276512"),
	("Neide Carvalho", "Praça da Liberdade, 12, Liberdade, São Paulo, SP", "11989827651, 11999872341"),
	("Maria Souza", "Rua dos Bandeirantes, 240, Centro, Pomedore, SC", "47994888221");

SELECT * FROM tb_clientes tcpf ;

/*
	Podemos aplicar a Primeira Forma Normal (1FN) na tabela tb_clientes seguindo os seguintes passos:
		- "Quebrar" a informação de endereço em múltiplas colunas (tipo_logradouro, numero, etc)
		- Remover a coluna multivalorada "telefone" para uma nova tabela de telefones (tb_telefones)
*/

-- Alterar o nome da tabela tb_clientes
ALTER TABLE tb_clientes RENAME TO tb_clientes_pre_1fn;

SELECT * FROM tb_clientes_pre_1fn;

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	tipo_logradouro TEXT NOT NULL,
	logradouro TEXT NOT NULL,
	numero TEXT NOT NULL,
	bairro TEXT NOT NULL,
	cidade TEXT NOT NULL,
	estado TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_telefones(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	cliente_id INTEGER NOT NULL,
	telefone TEXT NOT NULL,
	FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);

INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado
) VALUES
	("João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
	("Neide Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP");

SELECT * FROM tb_clientes tc ;

PRAGMA foreign_keys = ON;

INSERT INTO tb_telefones (cliente_id, telefone) VALUES
	(1, "47998276512"),
	(2, "11989827651"),
	(2, "11999872341");

SELECT * FROM tb_telefones;

-- Utilizamos INNER JOIN para mostrar dados de tabelas relacionadas
-- Abaixo mostramos os dados nome e cidade da tb_clientes, e telefone da tb_telefones
-- A cláusula WHERE é utilizada quando queremos limitar o resultado a determinado campo/regra
SELECT tc.nome, tc.cidade, tt.telefone FROM tb_clientes tc 
INNER JOIN tb_telefones tt
ON tc.id = tt.cliente_id WHERE tc.id = 1;

/*
 * Aplicamos a 1FN na tabela tb_clientes fazendo 2 coisas:
 * "Quebramos" o campo endereço em subcampos
 * O campo multivalorado "telefone" removemos da tabela e o colocamos em outra tabela
 * chamada tb_telefones, que é dependente da tabela tb_clientes (1:N)
 */


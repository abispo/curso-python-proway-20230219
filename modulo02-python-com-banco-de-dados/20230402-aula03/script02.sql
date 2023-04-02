/*
A segunda forma normal (2FN) exige que cada tabela possua uma chave primária única e que todas as outras colunas dependam
diretamente dessa chave primária. Isso ajuda a evitar problemas de redundância e inconsistência de dados em relação a registros
duplicados ou incompletos. Além disso, essa forma normal ajuda a melhorar a eficiência de consultas ao banco de dados, já que as
informações estão organizadas de forma mais estruturada.
*/

-- Comando para renomear uma coluna
-- ALTER TABLE table_name RENAME COLUMN current_name TO new_name;


-- tb_controle

CREATE TABLE IF NOT EXISTS tb_controle(
	id			INTEGER NOT NULL,
	servico_id	INTEGER NOT NULL,
	servico		TEXT	NOT NULL,
	total_horas	INTEGER	NOT NULL,
	valor_hora	REAL	NOT NULL,
	
	PRIMARY KEY(id, servico_id)
);

INSERT INTO tb_controle (id, servico_id, servico, total_horas, valor_hora) VALUES
	(1, 1, "Manutenção de PC", 6, 80),
	(2, 1, "Manutenção de PC", 10, 80),
	(3, 2, "Desenvolvimento de Site", 150, 100),
	(4, 3, "Configuração de Servidor", 30, 250),
	(5, 4, "Aulas de Programação", 80, 50);

SELECT * FROM tb_controle ;

/*
 * A tabela tb_controle não está na Segunda Forma Normal (2FN), pois parte das colunas (servico, valor_hora)
 * dependem apenas de 1 parte da chave primária (servico_id). Nesse caso, devemos remover essas colunas dessa
 * tabela e colocar em outra tabela (tb_servicos)
 */

CREATE TABLE IF NOT EXISTS tb_servicos(
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	valor_hora REAL NOT NULL
);

ALTER TABLE tb_controle RENAME TO tb_controle_pre_2fn;

CREATE TABLE IF NOT EXISTS tb_controle(
	id	INTEGER,
	servico_id INTEGER,
	total_horas	REAL NOT NULL,
	PRIMARY KEY(id, servico_id),
	FOREIGN KEY(servico_id) REFERENCES tb_servicos(id)
);

-- Criação da tabela tb_servicos que irá armazenar as informações de serviço

INSERT INTO tb_servicos (nome, valor_hora) VALUES
("Manutenção de PC", 80),
("Desenvolvimento de Site", 100),
("Configuração de Servidor", 250),
("Aulas de Programação", 50);

SELECT * FROM tb_servicos ts ;

INSERT INTO tb_controle (id, servico_id, total_horas) VALUES
(1, 1, 6),
(2, 1, 10),
(3, 2, 150),
(4, 3, 30),
(5, 4, 80);

SELECT * FROM tb_controle tc ;

/*
 * Selecionar os dados das tabelas tb_controle e tb_serviço
 * Abaixo criamos uma coluna somente-leitura com a informação do valor da hora vezes o total de horas
 */

SELECT ts.nome AS "Nome do Serviço", ts.valor_hora, tc.total_horas, ts.valor_hora * tc.total_horas as "Preço final"
FROM tb_servicos ts 
INNER JOIN tb_controle tc 
ON ts.id = tc.servico_id;

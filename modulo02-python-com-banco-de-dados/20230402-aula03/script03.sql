/*
A terceira forma normal (3FN) exige que cada coluna em uma tabela seja dependente apenas da chave primária da tabela, e
não de outras colunas. Isso ajuda a evitar problemas de redundância e inconsistência de dados em relação a informações
desnecessárias ou irrelevantes, e também ajuda a melhorar a eficiência de consultas ao banco de dados.
*/

-- tb_pedidos_itens

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id		INTEGER		NOT NULL,
	item_id			INTEGER		NOT NULL,
	valor_unitario	REAL		NOT NULL,
	quantidade		INTEGER		NOT NULL,
	subtotal		REAL		NOT NULL,
	PRIMARY KEY(pedido_id, item_id)
);

INSERT INTO tb_pedidos_itens (pedido_id, item_id, valor_unitario, quantidade, subtotal) VALUES
	(1, 1, 10, 2, 10 * 2),
	(1, 2, 3.50, 5, 3.50 * 5),
	(2, 3, 69.90, 2, 69.90 * 2);


SELECT * FROM tb_pedidos_itens ;

/*
 * A tabela tb_pedidos_itens não está na Terceira Forma Normal (3FN) pois a coluna subtotal depende dos valores
 * de outras colunas que não são chave-primária da tabela (valor_unitario, quantidade)
 * 
 * A tabela tb_pedidos_itens também não está na 2FN, pois o campo valor_unitario depende apenas de parte da
 * chave primária (item_id)
 */

-- Criamos a tabela tb_itens para armazenar as informações de item
CREATE TABLE IF NOT EXISTS tb_itens(
	id		INTEGER	PRIMARY KEY AUTOINCREMENT,
	nome	TEXT	NOT NULL,
	valor_unitario	REAL	NOT NULL
);

INSERT INTO tb_itens(nome, valor_unitario) VALUES
	("Desodorante", 10),
	("Sabonete", 3.50),
	("Aparelho de Barbear", 69.90);

ALTER TABLE tb_pedidos_itens RENAME TO tb_pedidos_itens_pre_3fn;

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id	INTEGER NOT NULL,
	item_id		INTEGER	NOT NULL,
	quantidade	INTEGER NOT NULL,
	PRIMARY KEY(pedido_id, item_id),
	FOREIGN KEY(item_id) REFERENCES tb_itens(id)
);

--DROP TABLE tb_pedidos_itens;

INSERT INTO tb_pedidos_itens (pedido_id, item_id, quantidade) VALUES
	(1, 1, 2),
	(1, 2, 5),
	(2, 3, 2);

INSERT INTO tb_pedidos_itens(pedido_id, item_id, quantidade) VALUES (3, 1, 4);

SELECT * FROM tb_pedidos_itens;

-- Vamos criar uma view que irá armazenar o resultado da consulta mostrando o subtotal do pedido

CREATE VIEW IF NOT EXISTS vw_total_pedidos AS
SELECT ti.nome, ti.valor_unitario, tpi.quantidade, ti.valor_unitario * tpi.quantidade as subtotal
from tb_itens ti 
INNER JOIN tb_pedidos_itens tpi
ON ti.id = tpi.item_id
ORDER BY subtotal DESC;


-- Chamando a VIEW
SELECT * FROM vw_total_pedidos ;

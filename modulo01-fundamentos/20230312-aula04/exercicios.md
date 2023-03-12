# Exercícios

1. Crie um script que abra o arquivo `nomes.txt` e leia o seu conteúdo. Depois de lido, você deve imprimir no terminal os 10 nomes que mais se repetem e a quantidade de vezes que eles se repetem na ordem do maior pro menor. Exemplo:
```
python ex01.py
Lista de nomes que mais se repetem:

Mariane: 10 vezes
Manuela: 9 vezes
Heitor: 6 vezes
.
.
.
```

Além disso, essas informações devem ser salvas em um arquivo csv (nomes.csv), que vai conter 2 colunas:
* nome
* quantidade

Dica: Salve os dados em um dicionário e utilize a função built-in `sorted()` para mostrar na ordem correta.

2. Crie um script que abra o arquivo `vendas.txt` e leio o seu conteúdo. O conteúdo do arquivo é formado por uma lista de informações sobre vendedores: O seu código, o seu nome e a quantidade de vendas realizadas em um período. O script deve mostrar no terminal as seguintes informações:
* Valor total de vendas (soma das vendas de todos os vendedores)
* Média total de vendas
* Lista dos maiores vendedores, do maior pro menor

Além disso, deve ser calculado o valor total da remuneração do vendedor de acordo com as seguintes regras:
* Vendedores que venderam menos de 5000, não recebem bônus
* Vendedores que venderam entre 5000 e 9999.99, recebem um bônus de 10%
* Vendedores que venderam entre 10000 e 14999.99, recebem um bônus de 20%
* Vendedores que venderam 15000 ou mais, recebem um bônus de 30%
Além disso, os 3 primeiros colocados recebem como um adicional no salário os seguintes valores, na ordem:
* 500 para o primeiro colocado em vendas
* 250 para o segundo colocado em vendas
* 125 para o terceiro colocado em vendas

Essas informações devem ser mostradas no terminal


3. Crie um script que abra o arquivo `notas.csv` e leia o seu conteúdo. O arquivo possui uma lista de nomes de alunos e as suas respectivas novas em trabalhos. Depois de ler esse arquivo, o script deve mostrar:
* A quantidade total de alunos
* A média geral
* Os 10 alunos com as maiores médias
Detalhe: As médias são calculadas excluindo a melhor e a pior nota de cada aluno. Ou seja, a média é calculada utilizando as 3 notas intermediárias.
Dica: Ordene as notas ou utilize as funções built-in `max()` e `min()` para saber quais são as melhores e as piores notas

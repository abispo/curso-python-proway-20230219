
# Criar estatísticas do sistema
    * Mostrar quantas perguntas estão cadastradas no sistema
    * Mostrar quantas opções estão cadastradas no sistema


## O que será necessário fazer?
    * Criar uma rota (/enquetes/estatisticas)
    * Criar uma função em views.py que seja chamada quando a rota for acessada
        * Criar a função e associar essa função a rota no arquivo urls.py do pacote
    * Criar o template que vai mostrar as informações (enquetes/estatisticas.html)

### Documentação do Django Query API
https://docs.djangoproject.com/en/4.2/ref/models/querysets/

---

# Pacote mensagens

Na página de resultados de uma enquete, serão mostrados comentários feitos para a enquete

1. Criar o pacote mensagens
    * `python manage.py startapp mensagens`

2. Registramos o pacote no arquivo `settings.py`, na lista `INSTALLED_APPS`

3. Criar o arquivo de urls (urls.py)

4. Esse pacote terá uma model chamada `Mensagem`, que terá a seguinte estrutura:
    * Um campo `email`, que não será obrigatório
    * Um campo `texto`, que representará a mensagem deixada (models.Text)
    * Um campo `data_hora`, que irá salvar a data e a hora que a mensagem foi criada
    * Um campo pergunta, que será uma chave estrangeira para a model Pergunta

5. (Até esse ponto, as mensagens podem ser criadas pelo admin). Na página de resultados da enquete, 
mostrar a lista com as mensagens pertencentes à pergunta

6. Criar uma rota para cadastro de nova mensagem. Quando a mensagem for salva, precisamos ter a informação
de qual pergunta essa mensagem pertence. Essa rota será chamada no link "Inserir comentário" na página
de resultado de enquete.
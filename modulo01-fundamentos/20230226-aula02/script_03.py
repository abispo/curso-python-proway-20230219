# Cópia de listas

if __name__ == "__main__":
    lista_cursos = ["Python", "C#", "PHP", "SQL", "Design"]
    nova_lista_cursos = lista_cursos

    nova_lista_cursos.pop(-1)

    # Nesse caso, a linha anterior também altera o "valor" do dicionário
    # lista_cursos, pois ambas as variáveis apontam para a mesma
    # posição de memória
    print(nova_lista_cursos)
    print(lista_cursos)

    # Para resolver isso, podemos utilizar 2 abordagens:
    # Utilizar o método copy()
    lista_cursos_inverno = lista_cursos.copy()
    lista_cursos_inverno.append("Golang")

    print(lista_cursos_inverno)

    # Podemos gerar também um novo valor utilizando o slice
    lista_cursos_primavera = lista_cursos_inverno[:]
    lista_cursos_primavera.append("Devops")

    print(lista_cursos)
    print(nova_lista_cursos)
    print(lista_cursos_inverno)
    print(lista_cursos_primavera)
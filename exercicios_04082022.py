# Validar notas da lista se estão entre os números 0 e 10, caso não, retorna a posição da lista com o número inválido
def validaNotas(notas: float) -> int:
    validation = 0
    for nota in notas:
        validation += 1
        if nota < 0 or nota > 10:
            return validation

    return 0

# Exclui o menor valor contido na lista
def excluiMenorNota(notas: list) -> list:
    menorNota = 10
    newList = []

    for nota in notas:  # loop para definir o menor valor contido na lista
        if nota < menorNota:
            menorNota = nota

    for nota in notas:  # loop para criar uma nova lista excluindo o menor valor definido anteriormente
        if nota > menorNota:
            newList.append(nota)

    return newList

''' Calcula a média dos números contidos na lista.
    Em relação aos exercícios, tomar cuidado aqui para inserir uma lista com notas validas, 
    para não gerar uma média válida'''
def calculaMedia(notas: list) -> float:
    somaNotas = 0
    media = 0
    for nota in notas:
        somaNotas += nota
    media = somaNotas / len(notas)

    return media


'''Dado uma nota, verificar se ela é válida (de 0 a 10). Exibir a mensagem "Nova válida" ou "Nota inválida'''
def exercicio01():
    nota = float(input("Digite a nota: ")) #Exemplo de uso: 3.1
    if validaNotas([nota]) == 0:
        print("Nota válida")
    else:
        print("Nota inválida")


'''Solicite a nota dos checkPoints, exclua a nova de menor valor e calcule a média'''
def exercicio02() -> bool:
    notas = [float(nota) for nota in input("Digite as notas: ").split()] #Exemplo de uso: 3.1 6.5 7.5
    validacao = validaNotas(notas)
    if validacao == 0:
        notas = excluiMenorNota(notas)
        media = calculaMedia(notas)
        print(media)
    else:
        print(f'{validacao}º nota inválida')


'''Verifique se o aluno está aprovado ou não (média de ao menos 6). Exibindo a mensagem: 
   - "Aprovado com média X" ou "Reprovado com media X"'''
def exercicio03():
    notas = [float(nota) for nota in input("Digite as notas: ").split()] #Exemplo de uso: 3.1 6.5 7.5
    if validaNotas(notas) == 0:
        notas = excluiMenorNota(notas)
        media = calculaMedia(notas)
        status = "testezinho"
        if media > 6:
            status = "Aprovado"
        else:
            status = "Reprovado"

        print(f'{status} com media {media}')
    else:
        print("Somente digite notas de 0 a 10")


'''Para os não aprovados, caso a média do aluno seja abaixo de 4, exibir a mensagem "Reprovado com media X"
   Se a média estiver entre 4.0 e 5.9, solicitar uma nota de recuperação, efetuar uma nova média
   (desta nova de recuperação com a média anterior). Caso a nova média seja menor que 5 exibir 
   "Reprovado no Exame com média X" senão exibir "Aprovado no exame com média X"'''
def exercicio04():
    notas = [float(nota) for nota in input("Digite as notas: ").split()]  #Exemplo de uso: 3.1 6.5 7.5
    if validaNotas(notas) == 0:
        notas = excluiMenorNota(notas)
        media = calculaMedia(notas)
        if media < 4:
            print(f'Reprovado com media {media}')
        elif 4 <= media < 6:
            novaNota = float(input("Digite a nota de recuperação: "))
            novaMedia = (media + novaNota) / 2
            if (novaMedia < 5):
                print(f'Reprovado no Exame com media {novaMedia}')
            else:
                print(f'Aprovado no Exame com media {novaMedia}')
        else:
            print(f'Aprovado com media {media}')
    else:
        print("Somente digite notas de 0 a 10")

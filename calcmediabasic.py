nota1mat = int(input('Insira sua nota de matemática: '))
nota2por = int(input('Insira sua nota de português: '))
nota3his = int(input('Insira sua nota de história: '))

somanota = nota1mat + nota2por + nota3his

maxnota = 30

media = somanota / maxnota * 10

print("Sua média final foi:", media)

if media >= 6.0:
    print("Parabéns! Você foi aprovado!")
else:
    print("Infelizmente você foi reprovado.")

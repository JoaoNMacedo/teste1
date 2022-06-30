
A = int(input('Digite o 1º lado do trinangulo:'))
B = int(input('Digite o 2º lado do trinangulo:'))
C = int(input('Digite o 3º lado do trinangulo:'))

if(A > 0) and (B > 0) and (C > 0):
      if (A + B > C) and (A + C > B) and (B + C > A):
          if A==B and B==C and C==A:
              print('Trinagulo EQUILATERO')
          else:
               if A!=B and B!=C and C!=A:
                  print('Triangulo ESCALENO')
               else:
                   print('Trinagulo ISOCELES')

      else:
          print('Um dos lados impossibilita a formação do trinagulo')
else:
    print('Um dos lados impossibilita a formação do trinagulo')




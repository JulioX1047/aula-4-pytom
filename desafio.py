print("SOMA=1")
print("SUBTRAÇÃO =2")
print("MULTIPLICAÇÃO =3")
print("DIVISÃO = 4 ")
print("SAINDO = 5 ")
listanumeros= []
def soma(valor):
  total = 0
  for valores in valor:
    total += valores
  print (f"A soma é de: {total}")

def subs(valor):
  total=0;
  for valores in valor:
    total-= valores
  print(f"A substração é  : {total}")  

def produto(valor):
  total=0
  for valores in valor :
    total*=valores
  print(f"Multiplicação é : {produto}")

def div(valor):
  total=0
  for valores in valor :
    total/=valores
  print(f" A divisão é : ")

opcao=int(input("DIGITE A OPERAÇÃO QUE VOCÊ QUER(1-5) "));


numeros = str(input("Digite um número: "))

for num in numeros.split():
  try:
    listanumeros.append(float(num))
  except:
    print ("Erro!")

if opcao==1:
  print(soma(listanumeros))
elif opcao==2:
  print(subs(listanumeros))  
elif opcao==3:
  print(produto(listanumeros))  
elif opcao==4:
  print(div(listanumeros))  
elif opcao==5:
  print("Saindo do programa ")
else:
  print("Opção invalida , saindo do programa ")    



hora = float(input("Diz o horario ai fera "));
def saudacao(horario):
  if horario >= 6 and horario <= 12:
    print("Bom dia !!!!!")
  elif horario >= 13 and horario <= 18:
    print("Boa tarde !!!!!")
  elif horario >= 19 or horario <= 5:
    print("Boa noite !!!!!")
  return saudacao
saudacao(hora)
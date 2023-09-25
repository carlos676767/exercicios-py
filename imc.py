peso = float(input("digite seu peso (em kg):"))
altura = float(input("digite sua altura (em altura):"))

imc = peso/(altura * altura)

if imc <= 18.5:
    print("voce esta abaixo do peso")
elif 18.6 <= imc <= 24.9:
    print("voce esta no peso ideal")
elif 25.0 <= imc <= 29.9:
    print("voce esta um pouco acima do peso.")
elif 30.0 <= imc <= 34:
    print("voce esta obesidade grau ||")
elif 35.0 <= imc <= 39.9:
    print("voce esta na obesidade severa")
else:
    print("voce esta na obesidade morbida")
    
    
    
    

    

def clasificacion_imc(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        return "bajo peso"
    elif imc < 25:
        return "peso normal"
    else:
        return "sobrepeso"

print(clasificacion_imc(70, 1.75))
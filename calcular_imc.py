def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        categoria = "bajo peso"
    else:
        if imc < 25:
            categoria = "Normal"
        else:
            categoria = "Obeso"
    return categoria

print(calcular_imc(70, 1.75))
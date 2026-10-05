def clasificar_nota(nota):
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

print(clasificar_nota(8))
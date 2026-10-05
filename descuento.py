def calcular_descuento(precio, porcentaje):
    if porcentaje > 50:
        precio_con_descuento = precio * 0.5
    else:
        precio_con_descuento = precio
    return precio_con_descuento

print(calcular_descuento(100, 60))
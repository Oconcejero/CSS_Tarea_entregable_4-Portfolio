def iva(factura):
    calculo=factura*21
    resultado=calculo/100
    total= factura+resultado
    return total

iva(1000)
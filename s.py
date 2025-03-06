def main():
    print("=== Cálculos según la lógica del Excel ===\n")
    
    # Entradas: se pide al usuario ingresar los valores requeridos.
    try:
        # Valor de la UIT (H4)
        H4 = float(input("Ingrese el Valor de la UIT (H4): "))
        
        # Renta Bruta obtenida (E4)
        E4 = float(input("Ingrese la Renta Bruta obtenida (E4): "))
        
        # Otras Rentas de Cuarta Categoría (E7)
        E7 = float(input("Ingrese Otras Rentas de Cuarta Categoría (E7): "))
        
        # Total Renta de Quinta Categoría (Planilla) (E8)
        E8 = float(input("Ingrese Total Renta de Quinta Categoría (Planilla) (E8): "))
        
        # Gastos deducibles 3 UIT (E11)
        E11 = float(input("Ingrese Gastos deducibles 3 UIT (E11): "))
        if E11 > H4 * 3:
            print(f"Error: E11 no puede ser mayor que H4 * 3 (es decir, {H4 * 3}).")
            return
        
        # ITF (E12)
        E12 = float(input("Ingrese ITF (E12): "))
        
        # Renta de fuente extranjera (E14)
        E14 = float(input("Ingrese Renta de fuente extranjera (E14): "))
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")
        return

    # Cálculos

    # E5: Deducción (20% de la Renta Bruta obtenida, limitado a H4*24)
    E5 = min(E4 * 0.2, H4 * 24)
    
    # E6: Renta Neta obtenida = E4 - E5
    E6 = E4 - E5

    # E9: Total Rentas de Cuarta y Quinta Categoría = E6 + E7 + E8
    suma_rentas = E6 + E7 + E8
    E9 = suma_rentas if suma_rentas != 0 else None

    # E10: Deducción de 7 UIT (hasta el límite del total renta de cuarta categoría)
    if E9 is not None:
        if E9 < H4 * 7:
            E10 = E9
        else:
            E10 = H4 * 7
    else:
        E10 = None

    # E13: Total Renta Neta de Trabajo = E9 - (E10 + E11 + E12)
    if E9 is not None:
        resta = E10 + E11 + E12
        diferencia = E9 - resta
        E13 = diferencia if diferencia != 0 else None
    else:
        E13 = None

    # E15: Total renta imponible de trabajo y fuente extranjera = E13 + E14
    if (E13 is not None) and (E14 is not None):
        E15 = E13 + E14
    else:
        E15 = None

    # Mostrar resultados
    print("\n=== Resultados ===")
    print(f"E5 (Deducción 20% o máximo H4*24): {E5:,.2f}" if E5 is not None else "E5: -")
    print(f"E6 (Renta Neta obtenida): {E6:,.2f}" if E6 is not None else "E6: -")
    print(f"E9 (Total Rentas de 4ta y 5ta Categoría): {E9:,.2f}" if E9 is not None else "E9: -")
    print(f"E10 (Deducción de 7 UIT): {E10:,.2f}" if E10 is not None else "E10: -")
    print(f"E13 (Total Renta Neta de Trabajo): {E13:,.2f}" if E13 is not None else "E13: -")
    print(f"E15 (Total renta imponible de trabajo y fuente extranjera): {E15:,.2f}" if E15 is not None else "E15: -")
    
if __name__ == '__main__':
    main()

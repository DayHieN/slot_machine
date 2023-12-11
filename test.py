def dibujar_carta(numero, palo):
    # Símbolos de los palos
    palo_simbolos = {'corazones': '♥', 'diamantes': '♦', 'treboles': '♣', 'picas': '♠'}

    # Dibujo de la carta
    carta = f"""
    +-----+
    |{numero:<2}   |
    |  {palo_simbolos[palo]}  |
    |   {numero:>2}|
    +-----+
    """

    print(carta)

# Ejemplo de uso
numero_carta = '10'
palo_carta = 'corazones'

dibujar_carta(numero_carta, palo_carta)
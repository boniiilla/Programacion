def escribir_frases():
    frases_guardadas = []
    frase = input("Escriu una frase: ")
    frases_guardadas.append(frase)
    return frase, frases_guardadas

def contador_a(frases_guardadas):
    max_a_en_frase = 0
    frase_con_mas_a = ""
    for frase in frases_guardadas:
        a_en_frase = 0
        for letra in range(len(frase)):
            if frase[letra].casefold() == "a":
                a_en_frase += 1
        if a_en_frase > max_a_en_frase:
            max_a_en_frase = a_en_frase
            frase_con_mas_a = frase
    return max_a_en_frase, frase_con_mas_a

def frases_a():
    frase = str
    while frase != "fi":
        frase, frases_guardadas = escribir_frases()
        max_a_en_frase, frase_con_mas_a = contador_a(frases_guardadas)
        print(f"La frase amb més 'a' és: {frase_con_mas_a}")
        print(f"Té {max_a_en_frase} 'a'")
    
frases_a()
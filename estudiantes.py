#PRE: Añadim una llista de usuaris amb la següent informació: Nom, Cognom, Edat, Nota1, Nota2, Nota3 (Notas con valor entre 0-10)
estudiantes = [("Carlos", "Bonilla", 18, 7, 6, 10), ("Ruben", "Rodriguez", 20, 6, 5, 9), ("Izan", "Lozano", 18, 1, 5, 8)]
"""
CODIGO PARA AÑADIR ESTUDIANTES AUTOMATICAMENTE:

nombre_estudiants = int(input("Introdueix el nombre de estudiants a afegir: "))
estudiants_afegits = 0
while estudiants_afegits < nombre_estudiants:
    estudiante = []
    nom = str(input("Nom: "))
    cognom = str(input("Cognom: "))
    edat = int(input("Edat: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    estudiante.append(nom)
    estudiante.append(cognom)
    estudiante.append(edat)
    estudiante.append(nota1)
    estudiante.append(nota2)
    estudiante.append(nota3)
    estudiantes.append(tuple(estudiante))
    estudiants_afegits += 1
    print(estudiantes)
"""


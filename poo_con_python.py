class Personaje:
    nombre = 'Default'
    fuerza = '0'
    inteligencia = '0'
    defensa = '0'
    vida = '0'
    #Indicar que no se haga nada en este momento
    pass
#variable de constructor vacío de la case
mi_personaje = Personaje()
mi_personaje.nombre = "minipekka"
mi_personaje.fuerza = 1
mi_personaje.inteligencia = 1
mi_personaje.defensa = 1
mi_personaje.vida = 1
print("El nombre del personaje es ",mi_personaje.nombre)
print("La fuerza de mi personaje es ", mi_personaje.fuerza)
print("La inteligencia de mi personaje es ", mi_personaje.inteligencia)
print("La defensa de mi personaje es ", mi_personaje.defensa)
print("La vida de mi personaje es ", mi_personaje.vida)
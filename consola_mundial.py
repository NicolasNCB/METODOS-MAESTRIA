"""
Ejercicio nivel 3: AnÃ¡lisis de jugadores FIFA previo al Mundial 
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas Prueba
* Diccionarios
* Archivos
@author: Cupi2
"""
import mundial as m

def ejecutar_cargar_datos() -> dict:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de los jugadores.
    Retorno: dict
        El diccionario de clubes con la informaciÃ³n de los jugadores en el archivo
    """
    jugadores = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con los ajugadores FIFA: ")
    jugadores = m.carga_de_datos(archivo)
    if len(jugadores) == 0:
        print("El archivo seleccionado no es valido. No se pudieron cargar los bloques.")
    else:
        print("Se cargaron los siguientes clubes con sus jugadores a partir del archivo.")
        for key in jugadores.keys():
            print(key)
    return jugadores

def ejecutar_equipos_con_cadena_nombre(jugadores:dict)->None:
    """Ejecuta la opcion de encontrar los equipos que tiene en su nombre 
    la cadena dada por parámetro.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'Los clubes que tienen la cadena ingresada en su nombre son: (lista con los nombres de los clubes)'
        Puede utilizar la conversión a list de las llaves del diccionario resultante. Por ejemplo,
        list(equipos_filtrados.keys())
    En caso de que ningún club tenga la cadena ingresada en su nombre, se debe retornar el mensaje:
        'No hay clubes que tengan en su nombre la cadena (cadena)'
        """
    cadena = input("Ingrese la cadena de carácteres: ")
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_calcular_promedio_salario(jugadores:dict) -> None:
    """Ejecuta la opcion de calcular el promedio del salario de un equipo.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El salario promedio del club (nombre del club) es (salario promedio) EUR.'
    En caso de que el nombre del club no exista, el mensaje debe decir:
        'No hay un club que tenga el nombre de (nombre)'
    """
    equipo = input("Ingrese el nombre del equipo/club del cual quiere conocer el salario promedio: ")
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_calcular_puntaje_jugador(jugadores:dict) -> None:
    """Ejecuta la opcion que calcula el puntaje de un jugador
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El puntaje del jugador (nombre del jugador) es (puntaje).'
    Si no existe un jugador con el nombre dado, se debe mostrar el mensaje:
        'El jugador (nombre del jugador) no existe'
    """
    jugador = input("Ingrese el nombre del jugador del cual quiere conocer su puntaje: ")
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_mejores_y_peores_jugadores(jugadores:dict) -> None:
    """Ejecuta la opcion que busca los mejores y peores jugadores segÃºn su puntaje.
    Se debe mostrar al usuario el diccionario resultante con todos los clubes y sus respectivos mejores y peores jugadores.
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_cantidad_jugadores_posicion(jugadores:dict) -> None:
    """Ejecuta la opcion que cuenta a los jugadores que juegan en una posicion determinada. 
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El numero de jugadores FIFA que juegan en la posicion (posicion) es (numero de jugadores).'
    """
    posicion = input("Ingrese la posicion que desea consultar: ")
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_jugadores_por_pais(jugadores:dict) -> None:
    """Ejecuta la opcion que muestra el pais al que pertenece cada jugador.
    Se debe mostrar al usuario el diccionario de paises con los nombres de los respectivos jugadores de cada pais.
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_top10_paises_reputacion_internacional(jugadores:dict) -> None:
    """Ejecuta la opcion que determina el top 10 de paises con mejor reputacion internacional.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'Los 10 paises con mejor reputacion internacional son (paises separados por coma).'
     """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de jugadores.")
    print("2. Consultar los equipos que tienen una cadena dada en su nombre")
    print("3. Calcular el promedio de salarios de los jugadores de un equipo.")
    print("4. Calcular el puntaje de un jugador.")
    print("5. Consultar el mejor y el peor jugador de cada equipo segun su puntaje.")
    print("6. Consultar cuantos jugadores juegan en una posicion determinada. ")
    print("7. Consultar los jugadores por pai­s/nacionalidad.")    
    print("8. Consultar el top 10 de paises con mejor reputacion internacional promedio.")
    print("9. Salir.") 

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    jugadores = {}
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opcion: "))
        if opcion_seleccionada == 1:
            jugadores = ejecutar_cargar_datos()
        elif opcion_seleccionada ==2:
            ejecutar_equipos_con_cadena_nombre(jugadores)
        elif opcion_seleccionada ==3:
            ejecutar_calcular_promedio_salario(jugadores)
        elif opcion_seleccionada ==4:
            ejecutar_calcular_puntaje_jugador(jugadores)
        elif opcion_seleccionada ==5:
            ejecutar_mejores_y_peores_jugadores(jugadores)
        elif opcion_seleccionada ==6:
            ejecutar_cantidad_jugadores_posicion(jugadores)
        elif opcion_seleccionada ==7:
            ejecutar_jugadores_por_pais(jugadores)
        elif opcion_seleccionada ==8:
            ejecutar_top10_paises_reputacion_internacional(jugadores)
        elif opcion_seleccionada ==9:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")


#PROGRAMA PRINCIPAL
iniciar_aplicacion()
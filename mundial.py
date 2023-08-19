 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:05:10 2022

@author: nicocaribana
"""
def carga_de_datos (ruta_archivo:str)->dict:

    archivo=open(ruta_archivo,"r")
    llaves=archivo.readline()[:-1].split(",")
    linea=archivo.readline().split(",")
    clubes={}
    while len(linea)>1:
            if linea[0] not in clubes:
                lista_jugadores=[]
                primer_jugador={}
                primer_jugador[llaves[1]]=linea[1]
                primer_jugador[llaves[2]]=linea[2]
                primer_jugador[llaves[3]]=linea[3]
                primer_jugador[llaves[4]]=linea[4]
                primer_jugador[llaves[5]]=linea[5]
                primer_jugador[llaves[6]]=linea[6]
                primer_jugador[llaves[7]]=linea[7]
                primer_jugador[llaves[8]]=linea[8]
                primer_jugador[llaves[9]]=linea[9]
                primer_jugador[llaves[10]]=linea[10]
                primer_jugador[llaves[11]]=linea[11]
                primer_jugador[llaves[12]]=linea[12]
                primer_jugador[llaves[13]]=linea[13][:-1]
                lista_jugadores.append(primer_jugador)
                clubes[linea[0]]=lista_jugadores
                linea=archivo.readline().split(",")
    
            else:
                jugador_nuevo={}
                jugador_nuevo[llaves[1]]=linea[1]
                jugador_nuevo[llaves[2]]=linea[2]
                jugador_nuevo[llaves[3]]=linea[3]
                jugador_nuevo[llaves[4]]=linea[4]
                jugador_nuevo[llaves[5]]=linea[5]
                jugador_nuevo[llaves[6]]=linea[6]
                jugador_nuevo[llaves[7]]=linea[7]
                jugador_nuevo[llaves[8]]=linea[8]
                jugador_nuevo[llaves[9]]=linea[9]
                jugador_nuevo[llaves[10]]=linea[10]
                jugador_nuevo[llaves[11]]=linea[11]
                jugador_nuevo[llaves[12]]=linea[12]
                jugador_nuevo[llaves[13]]=linea[13][:-1]
                clubes[linea[0]].append(jugador_nuevo)      
                linea=archivo.readline().split(",")
    
    archivo.close() 
    return(clubes)
diccionario=carga_de_datos("players.csv")
def equipos_con_cadena (cadena: str, jugadores: dict)-> dict:
    equipos_filtrados={}
    for llaves in jugadores.keys():
        if cadena in llaves:
            equipos_filtrados[llaves]=jugadores[llaves]
    return equipos_filtrados.keys()

def calcular_promedio_salario(nombre_equipo: str, clubes: dict)->str:
    if nombre_equipo not in clubes:
        salida="No hay un club que tenga el nombre"+" "+nombre_equipo
    else:
        salario_total=0
        
        for jugador in clubes[nombre_equipo]:
            salario_total+=int(jugador["wage"])
            numero_jugadores=len(clubes[nombre_equipo])
           
        salario_promedio=salario_total/numero_jugadores
        salida="El salario promedio del club "+nombre_equipo+" es "+str(round(salario_promedio,2))+" EUR"
    
    return salida  

def buscar_jugador (nombre:str, clubes:dict)->dict:
    jugador_encontrado=None
    for jugadores_equipo in clubes.values():
        a=0
        while a<len(jugadores_equipo):
          jugador=jugadores_equipo[a]
          if jugador["name"]==nombre:
              jugador_encontrado= jugadores_equipo[a]
          jugador=jugadores_equipo[a]

          a+=1    
        
    return jugador_encontrado

def calcular_puntaje_jugador(jugador:dict)->float:
    puntaje=0
    delanteros=["ST","LS","RS","LF","CF","RF"]
    posiciones_izq=["LWB","LB","LM","LW","LF","LS"]
    posiciones_der=["RWB","RB","RM","RW","RF","RS"]

    if jugador["position"]=="RES" or jugador["position"]=="SUB":
        puntaje=0
    elif jugador["position"] in delanteros:
        puntaje=int(jugador["pace"])*0.1+int(jugador["shooting"])*0.45+int(jugador["passing"])*0.05+int(jugador["dribbling"])*0.4
    else:
        puntaje=int(jugador["pace"])*0.3+int(jugador["shooting"])*0.1+int(jugador["passing"])*0.4+int(jugador["dribbling"])*0.2
    if jugador["position"] in posiciones_izq and jugador["preferred_foot"]=="Left" or jugador["position"] in posiciones_der and jugador["preferred_foot"]=="Right":
        puntaje+=0.05

    return round(puntaje)
def mejores_y_peores_jugadores(clubes:dict)->dict:
    llaves=[]
    valores_max=[]
    valores_min=[]
    dict_final={}
    for nombres in clubes:
        llaves.append(nombres)  
    for jugadores in clubes.values():
        a=0
        lista_puntajes=[]
        while a<len(jugadores):
            lista_puntajes.append(calcular_puntaje_jugador(jugadores[a]))
            if len(jugadores)==len(lista_puntajes):
                valores_max.append(jugadores[lista_puntajes.index(max(lista_puntajes))])
                valores_min.append(jugadores[-1])

            a+=1
    for i in range(len(llaves)):
        dict_final[llaves[i]]={"mejor":valores_max[i]["name"],"peor":valores_min[i]["name"]}
        
    return dict_final["FC Barcelona"]
               
        
               
               
        
            
        

print(mejores_y_peores_jugadores(diccionario))

    
 
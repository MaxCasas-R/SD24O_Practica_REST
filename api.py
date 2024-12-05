from fastapi import FastAPI, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os 
import uuid
import orm.repo as repo
from sqlalchemy.orm import Session
from orm.config import generador_sesion

app=FastAPI() #con esto creamos el servidor 

#Ponemos un decorador
@app.get("/")
def inicio():
    print("Practica de FastApi con SQL, Max Casas")
    respuesta={
        "mensaje":"Practica de FastApi, Sistemas Distribuidos, HOLA MUNDO! Por:Max Casas:)"
    }
    return respuesta

#---------------Peticiones a Alumnos
#get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API devolviendo la lista de Alumnos")
    return repo.devuelve_alumnos(sesion)

# get("/alumnos/{id})
@app.get("/alumnos/{id}")
def alumno_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando alumno por Id")
    return repo.alumno_por_id(sesion,id)

# get("/alumnos/{id}/calificaciones")
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_idAlumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones por alumno Id")
    return repo.calificacion_por_idAlumno(sesion, id)

#get("/alumnos/{id}/fotos")
@app.get("/alumnos/{id}/fotos")
def fotos_por_idAlumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos por IdAlumno")
    return repo.foto_por_idAlumno(sesion,id)
#------------Peticion a fotos

#get("/fotos/{id}”)
@app.get("/fotos/{id}")
def fotos_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos por id")
    return repo.foto_por_id(sesion, id)

#----------Peticion a calificaciones
#get("/calificaciones/{id}”)
@app.get("/calificaciones/{id}")
def calificaciones_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones por id")
    return repo.calificacion_por_id(sesion, id)

#Le dejamos hasta aquí por hoy:)
#delete("/fotos/{id}”)
#delete("/calificaciones/{id}”)
#delete("/alumnos/{id}/calificaciones")
#delete("/alumnos/{id}/fotos")
#delete("/alumnos/{id})
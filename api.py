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

#----------------Sección de deletes
#delete("/fotos/{id}”) #crearemos una nueva consulta en repo.py para borrar por id de foto
@app.delete("/fotos/{id}")
def borrar_foto_porId(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando foto por id")
    repo.borrar_foto_por_iD(sesion, id)
    return {"Foto borrada por id", "Si!"}

#delete("/calificaciones/{id}”)
@app.delete("/calificaciones/{id}")
def borrar_cali_porId(id:int,sesion:Session=Depends(generador_sesion)):
    print("Borrando calificacion por iD")
    repo.borrar_calif_por_iD(sesion, id)
    return {"Calificaciones borradas por id", "Éxito!"}

#delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def borrar_cali_por_idAlumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando calificacion por idAlumno")
    repo.borrar_calificacion_por_idAlumno(sesion, id)
    return {"Calificaciones borradas por id alumno", "Amarillo amarillo lo platano"}

#delete("/alumnos/{id}/fotos")
@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_por_iDAlumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando fotos por idAlumno")
    repo.borrar_foto_por_idAlumno(sesion,id)
    return {"Fotos_borradas por id Alumnos", "Yeah"}

#delete("/alumnos/{id})
@app.delete("/alumnos/{id}")
def borrar_alumno_porId(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando alumno por Id")
    repo.borrar_calificacion_por_idAlumno(sesion,id)
    repo.borrar_foto_por_idAlumno(sesion,id)
    repo.borrar_por_idAlumno(sesion,id)
    return {"Alumno_borrado", "yupi"}

#terminado:)
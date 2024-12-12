from fastapi import FastAPI, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os 
import uuid
import orm.repo as repo
from sqlalchemy.orm import Session
from orm.config import generador_sesion
import orm.esquemas as esquemas

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

#post("/alumno") para insertar un nuevo alumno
@app.post("/alumno")
def nuevo_alumno(id:int, info_alumno:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    print("Creando nuevo alumno")
    return repo.guardar_alumno(sesion,id, info_alumno)

#put("/alumno/{id}") Para actualizar un alumno por id
@app.put("/alumno/{id}")
def actualizar_alumno(id:int, info_alumno:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    print("Actualizando alumno por id")
    return repo.actualiza_alumno(sesion, id, info_alumno)

#------------Peticion a fotos

#get("/fotos/{id}”)
@app.get("/fotos/{id}")
def fotos_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos por id")
    return repo.foto_por_id(sesion, id)

#post("/alumnos/{id}/fotos") para insertar una nueva foto
@app.post("/alumnos/{id}/fotos")
def guardar_foto(id:int, foto:esquemas.FotoBase, sesion:Session=Depends(generador_sesion)):
    print("Guardando foto")
    return repo.guardar_foto_alumnoid(sesion, id, foto)

#put("/fotos/{id}") para actualizar una foto por id
@app.put("/fotos/{id}")
def actualiza_foto(id:int, info_foto:esquemas.FotoBase, sesion:Session=Depends(generador_sesion)):
    print("Actualizando foto por id")
    return repo.actualiza_foto_por_id(sesion, id, info_foto)

#----------Peticion a calificaciones
#get("/calificaciones/{id}”)
@app.get("/calificaciones/{id}")
def calificaciones_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones por id")
    return repo.calificacion_por_id(sesion, id)

@app.post("/alumnos/{id}/calificaciones") #para insertar una nueva calificacion en un alumno
def guardar_calificacion(id:int, calif:esquemas.CalificacionBase, sesion:Session=Depends(generador_sesion)):
    print("Guardando calificacion")
    return repo.guardar_calificacion(sesion, id, calif)

@app.put("/calificaciones/{id}") #para actualizar una calificacion por id
def actualiza_calificacion(id:int, info_calif:esquemas.CalificacionBase, sesion:Session=Depends(generador_sesion)):
    print("Actualizando calificacion por id")
    return repo.actualiza_calificacion(sesion, id, info_calif)
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
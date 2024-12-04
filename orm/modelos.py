from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, ForeignKey
import datetime

class Alumno(BaseClass):
    __tablename__="usuarios" #Nombre de la tabla
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column(String(100))
    password=(Column(100))
    fecha_registro=Column(datetime(timezone=True),default=datetime.datetime.now)

class Calificacion(BaseClass):
    id=Column(Integer,primary_key=True)
    id_alumno=Column(Integer,ForeignKey(Alumno.id))
    uea=Column(String(100))
    calificacion=Column(String(100))

class Foto(BaseClass):
    id=Column(Integer,primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(100))
    

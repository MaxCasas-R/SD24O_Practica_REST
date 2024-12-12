from pydantic import BaseModel

class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

#esquemas nuevos
class CalificacionBase(BaseModel):
    id_alumno:int
    uea:str
    calificacion:str


class FotoBase(BaseModel):
    titulo:str
    descripcion:str
    ruta:str


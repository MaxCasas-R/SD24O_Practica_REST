import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_


#--------------------Peticiones a alumnos
#Select * from app.usuarios
def devuelve_alumnos(sesion:Session):
    print("Devolviendo todos los alumnos")
    return sesion.query(modelos.Alumno).all()

#SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_por_id(sesion:Session, id_usuario:int):
    print("Devolviendo alumno por id")
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_usuario).firts()

#---------------------Peticiones a fotos
#SELECT * FROM app.fotos
def devuelve_fotos(sesion:Session):
    print("Devolviendo todas las fotos")
    return sesion.query(modelos.Foto).all()

#SELECT * FROM app.fotos WHERE id={id_fo}
def foto_por_id(sesion:Session, id_foto):
    print("Devolviendo foto por if")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def foto_por_idAlumno(sesion:Session, id_alumno:int):
    print("Devolviendo foto por id_alumno")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).first()

#-----------------------Peticiones a calificaciones
#Le dejamos por hoy aqui:)

import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

#--------------------Peticiones a alumnos
#Select * from app.usuarios
def devuelve_alumnos(sesion:Session):
    print("Devolviendo todos los alumnos")
    return sesion.query(modelos.Alumno).all()

#SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_por_id(sesion:Session, id_al:int):
    print("Devolviendo alumno por id")
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_al).first()

#-----DELETE------
#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def borrar_por_idAlumno(sesion:Session, id_al:int):
    print("Borrando alumno por id_Alumno")
    alm=alumno_por_id(sesion, id_al) #llamamos a la funcion alumno_por_id para comprobar que exista el usuario, para despues borrar
    if alm is not None:
        sesion.delete(alm) #pasamos la variable de la busqueda "Alm"
        sesion.commit() #confirmamos cambios
    respuesta={
        "mensaje":"Usuario eliminado"
    }
    return respuesta

#-----------------------Peticiones a calificaciones
#select * from calificaciones 
def devuelve_calificaciones(sesion:Session):
    print("Devolviendo calificaciones")
    return sesion.query(modelos.Calificacion).all()

#SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificacion_por_id(sesion:Session, id_calificacion:int):
    print("Devolviendo calificaciones por id")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first()

#SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificacion_por_idAlumno(sesion:Session, id_al:int):
    print("Devolviendo calificacion por Id_Alumno")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_al).all()

#-----DELETE------
#DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def borrar_calificacion_por_idAlumno(sesion:Session, id_al:int):
    print("Borrando calificacion por id del alumno")
    alm=calificacion_por_idAlumno(sesion, id_al) #Llamamos a funcion
    if alm is not None:
        for calificaciones_alumno in alm:
            sesion.delete(calificaciones_alumno)
            sesion.commit()
    respuesta={
        "mensaje":"calificacion borrada por id_Alumno"
    }
    return respuesta


#---------------------Peticiones a fotos
#SELECT * FROM app.fotos
def devuelve_fotos(sesion:Session):
    print("Devolviendo todas las fotos")
    return sesion.query(modelos.Foto).all()

#SELECT * FROM app.fotos WHERE id={id_fo}
def foto_por_id(sesion:Session, id_foto):
    print("Devolviendo foto por id")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def foto_por_idAlumno(sesion:Session, id_al:int):
    print("Devolviendo foto por id_alumno")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_al).all()

#-------------DELETES--------------
#DELETE FROM app.fotos WHERE id_alumnos={id_al}
def borrar_foto_por_idAlumno(sesion:Session ,id_al:int):
    print("Borrando foto por idAlumno")
    alm=foto_por_idAlumno(sesion, id_al) #llamamos a la funcion
    if alm is not None:
        for fotos_alumno in alm:
            sesion.delete(fotos_alumno)
            sesion.commit()
    respuesta={
        "mensaje":"Se ha eliminado la foto"
    }
    return respuesta
#delete from app.fotos where id_foto=id
def borrar_foto_por_iD(sesion:Session, id:int):
    print("Borrando foto por Id")
    alm=foto_por_id(sesion, id)
    if alm is not None:
        sesion.delete(alm)
        sesion.query()

    respuesta={
        "mensaje":"Se ha eliminado la foto"
    }
    

def borrar_calif_por_iD(sesion:Session, id:int):
    print("Borrando calificacion por id")
    alm=calificacion_por_id(sesion,id)
    if alm is not None:
        sesion.delete(alm)
        sesion.query()
    respuesta={
        "mensaje":"Se ha eliminado la calificacion por Id"
    }
    

#terminado
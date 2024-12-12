import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_
import orm.esquemas as esquemas

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


#---------POST Y PUT
#post("/alumnos")
def guardar_alumno(sesion:Session, id_alumno:int,alumno_esquema:esquemas.AlumnoBase):
    print("Insertando en alumnos un nuevo alumno")
    alumno=alumno_por_id(sesion, id_alumno)
    if alumno is None:
        alumno_bd = modelos.Alumno(
            id=id_alumno,
            nombre=alumno_esquema.nombre,
            edad=alumno_esquema.edad,
            domicilio=alumno_esquema.domicilio,
            carrera=alumno_esquema.carrera,
            trimestre=alumno_esquema.trimestre,
            email=alumno_esquema.email,
            password=alumno_esquema.password
        )
        sesion.add(alumno_bd)
        sesion.commit()
        sesion.refresh(alumno_bd)
        return alumno_bd
    else:
        respuesta = {"Mensaje": "El alumno ya existe"}
        return respuesta
    
#put("/alumnos/{id}")
def actualiza_alumno(sesion:Session, id_alumno:int, alumno_esquema:esquemas.AlumnoBase):
    print("Actulizando alumno")
    #comprobamos si existe el alumno
    alm_bd=alumno_por_id(sesion, id_alumno)
    #Y actualizamos
    if alm_bd is not None:
        alm_bd.nombre=alumno_esquema.nombre
        alm_bd.edad=alumno_esquema.edad
        alm_bd.domicilio=alumno_esquema.domicilio
        alm_bd.carrera=alumno_esquema.carrera
        alm_bd.trimestre=alumno_esquema.trimestre
        alm_bd.email=alumno_esquema.edad
        alm_bd.password=alumno_esquema.password
        sesion.commit()
        sesion.refresh(alm_bd)
        print(alumno_esquema)
        return alumno_esquema
    else:
        respuesta={"Mensaje":"Usuario no encontrado"}
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

#post("/alumnos/{id}/calificaciones")
def guardar_calificacion(sesion:Session, id_alumno:int,calif_esquema:esquemas.CalificacionBase ):
    print("Insertando calificacion en un alumno")
    calificacion_bd=modelos.Calificacion(
        id_alumno=id_alumno,
        uea=calif_esquema.uea,
        calificacion=calif_esquema.calificacion
    )
    sesion.add(calificacion_bd)
    sesion.commit()
    sesion.refresh(calificacion_bd)
    return calificacion_bd

#put("/calificaciones/{id}")
def actualiza_calificacion(sesion:Session, id_calificacion:int, calif_esquema:esquemas.CalificacionBase):
    print("Actualizando calificacion por id")
    #comprobamos si existe la calificacion por su id
    cali_bd=calificacion_por_id(sesion, id_calificacion)
    if cali_bd is not None:
        cali_bd.uea=calif_esquema.uea
        cali_bd.calificacion=calif_esquema.calificacion
        sesion.commit()
        sesion.refresh(cali_bd)
        print(calif_esquema)
        return calif_esquema
    else:
        respuesta={"Mensaje":"Calificacion no encontrada"}
        return respuesta


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

#post("/alumnos/{id}/fotos")
def guardar_foto_alumnoid(sesion: Session, id_alumno: int, foto_esquema: esquemas.FotoBase):
    print("Insertando en alumno una nueva foto")
    alumno = alumno_por_id(sesion, id_alumno)
    if alumno is not None:
        foto_bd = modelos.Foto(
            titulo=foto_esquema.titulo,
            descripcion=foto_esquema.descripcion,
            ruta=foto_esquema.ruta,
            id_alumno=id_alumno
        )
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {"Mensaje": "El alumno no existe"}
        return respuesta

#put("/fotos/{id}")
def actualiza_foto_por_id(sesion:Session, id_foto:int, foto_esquema:esquemas.FotoBase):
    print("Actualizando foto por id")
    foto_bd=foto_por_id(sesion, id_foto)
    if foto_bd is not None:
        foto_bd.titulo=foto_esquema.titulo
        foto_bd.descripcion=foto_esquema.descripcion
        foto_bd.ruta=foto_esquema.ruta
        sesion.commit()
        sesion.refresh(foto_bd)
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta={"Mensaje":"Foto no encontrada"}
        return respuesta

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
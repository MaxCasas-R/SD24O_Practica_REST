from sqlalchemy import create_engine #conexion a bd
from sqlalchemy.orm import sessionmaker #para hacer las sesiones 
from sqlalchemy.ext.declarative import declarative_base #base para mapear bd
import os 
#esto va a servir para configurar la bd. importando el modelo de la bd
from orm import modelos

#1.- Configuramos la conexion, y creamos la url de la bd
#URL_BD="postgresql://usuario_ejemplo:18112003@localhost:5432/practica"
#engine =create_engine(URL_BD,connect_args={"options":"-csearch_path=app"})
#conexion a la base de datos que aun no esta creada 
engine =create_engine(os.getenv("db_uri", "sqlite://base-ejemplo.db"))
modelos.BaseClass.metadata.create_all(engine)



#Obtenemos clase para crear objetos tipo sesion
SessionClass=sessionmaker(engine)

def generador_sesion():
    sesion=SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()



#terminado 
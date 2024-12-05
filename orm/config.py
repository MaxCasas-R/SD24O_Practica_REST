from sqlalchemy import create_engine #conexion a bd
from sqlalchemy.orm import sessionmaker #para hacer las sesiones 
from sqlalchemy.ext.declarative import declarative_base #base para mapear bd

#1.- Configuramos la conexion, y creamos la url de la bd
URL_BD="postgresql://usuario_ejemplo:18112003@localhost:5432/practica"

engine =create_engine(URL_BD,connect_args={"options":"-csearch_path=app"})

#Obtenemos clase para crear objetos tipo sesion
SessionClass=sessionmaker(engine)

def generador_sesion():
    sesion=SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()

BaseClass=declarative_base()


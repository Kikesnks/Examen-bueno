from django.db import models
import oracledb

# Create your models here.

class Plantilla:
    def __init__(self):
        self.nombreHosp = ""
        self.scod = 0
        self.empno = 0
        self.apellido = ""
        self.funcion = ""
        self.turno = ""
        self.salario = 0
    
class Hospital:
    def __init__(self):
        self.cod = 0
        self.nombre = ""

class ServicioPlantilla():
        self.conexion = oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")
    
    def getPlantilla(self, id):
        cursor = self.conexion.cursor()
        sql ="select NOMBRE from HOSPITAL where HOSPITAL_COD = :cod"
        cursor.execute(sql, (id,))
        hosp = cursor.fetchone()
        name = hosp[0]
        sql = "select * from PLANTILLA where HOSPITAL_COD = :cod"
#        hospital = Hospital()
        cursor.execute(sql, (id,))
        listaPlantilla = []
        for dato in cursor:
            plant = Plantilla()
            plant.nombreHosp = name
            plant.scod = dato[1]
            plant.empno = dato[2]
            plant.apellido = dato[3]
            plant.funcion = dato[4]
            plant.turno = dato[5]
            plant.salario = dato[6]
            listaPlantilla.append(plant)
        
        cursor.close()
        return listaPlantilla
    
    def getNombreHospital(self, id):
        sql = "select NOMBRE from HOSPITAL where HOSPITAL_COD = :cod"
        cursor = self.conexion.cursor()
        cursor.execute(sql, (id,))
        hosp = cursor.fetchone()
#        hospital = Hospital()
        hospital = hosp[0]
#        hospital.nombre = hosp[1]
        cursor.close()
        return hospital

    def getListaHospitales(self):
        sql ="select NOMBRE, HOSPITAL_COD from HOSPITAL"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        listaHospitales = []
        for hospital in cursor:
            hosp = Hospital()
            hosp.nombre = hospital[0]
            hosp.cod = hospital[1]
            listaHospitales.append(hosp)
        cursor.close()
        return listaHospitales
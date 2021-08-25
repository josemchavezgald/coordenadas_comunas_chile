import pymysql

class Connector:

    def __init__(self):
        self.connect = pymysql.connect(
            host='host.datari.net',
            user='admdatar_datari_api',
            password='qPdfQtZUxYlf',
            db='admdatar_api_datari'
        )

        self.cursor = self.connect.cursor()

    def get_region_id(self,query):
        self.cursor.execute(query)
        region =  self.cursor.fetchone()
        id_region = region[0]

        return id_region
    
    def get_comuna(self, query):

        self.cursor.execute(query)
        comuna = self.cursor.fetchone()
        if len(comuna) != 0:
            return comuna
        else:
            print('No existe comuna')
            retun -1

    def get_comuna_by_codigo(self,codigo):

        query = "SELECT * FROM datari_comuna WHERE cod_ut = "+str(codigo)

        self.cursor.execute(query)
        comuna = self.cursor.fetchone()
        if len(comuna) != 0:
            print(comuna)
            return comuna[0]
        else:
            print('No existe comuna')
            return -1

    def update_coordinates_comuna(self,lat,lon,codigo):

        query = "UPDATE datari_comuna SET lat = {0}, lon = {1} WHERE cod_ut = {2}"
        query = query.format(lat,lon,codigo)

        if(lat != 0 and lon != 0):
            try:
                self.cursor.execute(query)
                self.connect.commit()
                print('Datos Actualizados.')
                return 0
            except:
                self.connect.rollback()
                print('Error al ingresar tabla.')
                return -1



    def update_comuna(self,id_comuna,cod_ut):

        query = "UPDATE datari_comuna SET codigo={0} WHERE id = {1}"
       
        try:
            self.cursor.execute(query.format(cod_ut,id_comuna))
            self.connect.commit()
            print('Fila Ingresada.')
            return 0
        except:
            self.connect.rollback()
            print('Error al ingresar tabla.')
            return -1
        

    def close(self):

        return self.connect.close()
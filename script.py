__version__ = '0.1'
__author__ = 'JoseChGal'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import connector

#Objetivo: convierte coordenadas en formato (grados-minutos-segundos) a decimal
#-18°27'18" -> -18.455
def convert_to_decimal_coordinates(coordinates):
	decimal_coordinate = 0
	temp = coordinates.split('°')
	degrees = int(temp[0])
	temp = temp[1].split("\'")
	minutes = float(temp[0])
	temp = temp[1].split('"')
	seconds = float(temp[0])

	
	decimal_minutes = float(minutes/60)
	decimal_seconds = float(seconds/3600)

	if(degrees < 0):
		decimal_coordinate = degrees-(decimal_minutes+decimal_seconds)
	else:
		decimal_coordinate = degrees+(decimal_minutes+decimal_seconds)
	
	return decimal_coordinate

#Objetivo: Usando Selenium se accede al sitio web con la tabla y comienza a extraer los datos:
#codigos de comunas y sus respectivas latitud y longitud
#Ejemplo:
#CUT 	Nombre	Latitud 	Longitud
#15101 	Arica 	-18°27'18" 	-70°17'24" 
#
#
#Convierte latitudes y longitudes en grados-minutos-segundos a decimal.
#Devuelve un arreglo con 346 comunas donde cada comuna tiene un codigo, latitud y longitud	
def get_data(url):

	browser = webdriver.Chrome(ChromeDriverManager("2.36").install())
	timeout = 2

	browser.get(url) 

	print('Extrayendo data...')

	codigos = browser.find_elements_by_xpath('.//*[@id="mw-content-text"]/div[1]/table/tbody/tr/td[1]')
	lat = browser.find_elements_by_xpath('.//*[@id="mw-content-text"]/div[1]/table/tbody/tr/td[11]')
	lon = browser.find_elements_by_xpath('.//*[@id="mw-content-text"]/div[1]/table/tbody/tr/td[12]')

	cantidad_codigos = len(codigos)

	data_url = []

	if (len(lat) == len(lon)):
		if(len(lat) == len(codigos)):

			for i in range(0,cantidad_codigos):
				codigo = codigos[i].text
				latitud_temp = lat[i].text
				longitud_temp = lon[i].text

				convert_decimal_coordinates(latitud_temp)

				data = {
					'codigo': int(codigo),
					'latitud': convert_decimal_coordinates(latitud_temp),
					'longitud': convert_decimal_coordinates(longitud_temp)
				}

				data_url.append(data)

	try:
		myElem = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, 'bt')))
		browser.execute_script("bp(26834)")

	except TimeoutException:
		print("Se vencio el timeout")

	except Exception:
		browser.close()

	browser.close()

	return data_url
		




data = get_data('https://es.wikipedia.org/wiki/Anexo:Comunas_de_Chile')

print(data)



#Se puede agregar un conector alternativo (API Rest o Conexion a otro tipo de BD (NoSQL, SQL))

#Connector para MySQL usando libreria pymysql
# connector = connector.Connector()

# for dato in data:
# 	connector.update_coordinates_comuna(dato['latitud'],dato['longitud'],dato['codigo'])



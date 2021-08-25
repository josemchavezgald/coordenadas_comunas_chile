# Extracción latitud y longitud 346 comunas de Chile.

El siguiente script permite obtener las laitudes y longitudes de las comunas de Chile desde la pagina web 
```
https://es.wikipedia.org/wiki/Anexo:Comunas_de_Chile
```

utilizando Selenium se extraen los datos de la tabla generando una lista de diccionarios con los datos de las comunas.

Las latitudes que se encuentran en el sitio web estan en formato:
Grados-Minutos-Segundos
	
	```
	-18°27'18" 
	```

También se pueden convertir a decimal usando la función 
	
	```
	convert_to_decimal_coordinates(coordenadas)
	```
las comunas estan indexadas bajo su Código Único Territorial (CUT)

Se genera el archivo:

	```
	comunas_coordenadas.json
	```
		
	```
	[
		{
			codigo: 15101,
			latitud: -18.455,
			longitud: -70.29
		},
		...
	]
	```


### Pre-requisitos 📋

Iniciar ambiente virtual (virtualenv, pipenv)

Instalar librerias script

```
pip install -r requirements.txt
```

## Ejecución ⚙️

```
python script.py
```




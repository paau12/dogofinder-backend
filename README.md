# dogofinder-backend
DogoFinder platform - Minimum Viable Product Back-End (API)


## Mascotas

Detalles sobre la clase Mascota.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**
Retorna los campos de un objeto Mascota dado un id.
`GET api/v1/mascotas/id`

**respuesta:**
- Si se encuentra un objeto con el id dado:
```json
[
    {
	"nombre_mascota":String,
	"tipo_mascota":String,
	"raza_mascota":String,
	"descripcion_mascota":String,
	"codigo_qr":String,
	"foto_mascota":Image,
	"in_home":Bool,
	"id_usuario": Integer,
    }
]
```
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto mascota de la base de datos dado un id.
`DELTE api/v1/mascotas/id`

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Re-escribe los campos de un objeto mascota dado un id.
`PUT api/v1/mascotas/id`

**Parametros**
```json
[
    {
	"nombre_mascota":String,
	"tipo_mascota":String,
	"raza_mascota":String,
	"descripcion_mascota":String,
	"codigo_qr":String,
	"foto_mascota":Image,
	"in_home":Bool,
	"id_usuario": Integer,
    }
]
```

**respuesta:**
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Retorna todas las mascotas en la tabla.
`GET api/v1/mascotas/`

**respuesta:**
- Por cada objeto en la tabla:
```json
[
    {
	"nombre_mascota":String,
	"tipo_mascota":String,
	"raza_mascota":String,
	"descripcion_mascota":String,
	"codigo_qr":String,
	"foto_mascota":Image,
	"in_home":Bool,
	"id_usuario": Integer,
    },
    ...
]
```
- `400 Bad Request` si la petición esta mal formulada

Inserta un nuevo objeto mascota a la tabla.
`POST api/v1/mascotas/`

Campos del objeto:
```json
[
    {
	"nombre_mascota":String,
	"tipo_mascota":String,
	"raza_mascota":String,
	"descripcion_mascota":String,
	"codigo_qr":String,
	"foto_mascota":Image,
	"in_home":Bool,
	"id_usuario": Integer,
    },
    ...
]
```

**respuesta:**
- `201 Created` si el objeto es almacenado correctamente
- `400 Bad Request` si la petición esta mal formulada


## Mascota Perdida

Detalles sobre la clase Mascota_perdida.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**

Retorna los campos de un objeto Mascota_perdida dado un id.
`GET api/v1/mascota_perdida/id`

**respuesta:**
```json
[
	{
		"id_mascota_perdida":Integer,
		"id_mascota":Integer,
	}
]
```
- `404 Not Found` si el identificador no existe

Modifica los campos de un objeto Mascota_perdida dado un id
`PUT api/v1/mascota_perdida/id`

**Parametros**
```json
[
	{
		"id_mascota_perdida":Integer,
		"id_mascota":Integer,
	}
]
```

**respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto Mascota_perdida de la tabla
`DELETE api/v1/mascota_perdida/id`

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Retorna todas las mascotas perdidas en la tabla.
`GET api/v1/mascota_perdida/`

**respuesta:**
```json
[
	{
		"id_mascota_perdida":Integer,
		"id_mascota":Integer,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Agrega un objeto Mascota_perdida a la tabla
`POST api/v1/mascota_perdida/`

Campos del objeto:
```json
[
	{
		"id_mascota_perdida":Integer,
		"id_mascota":Integer,
	}
]
```

**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


## Mascota Encontrada

Detalles sobre la clase Mascota_encontrada.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**

Retorna los campos de un objeto Mascota_encontrada dado un id.
`GET api/v1/mascota_encontrada/id`

**respuesta:**
```json
[
	{
		"id_ascota_encontrada":Integer,
		"id_mascota":Integer,
	}
]
```
- `404 Not Found` si el identificador no existe

Modifica los campos de un objeto Mascota_encontrada dado un id
`PUT api/v1/mascota_encontrada/id`

**Parametros**
```json
[
	{
		"id_mascota_encontrada":Integer,
		"id_mascota":Integer,
	}
]
```

**respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto Mascota_encontrada de la tabla
`DELETE api/v1/mascota_encontrada/id`

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Retorna todas las mascotas encontradas en la tabla.
`GET api/v1/mascota_encontrada/`

**respuesta:**
```json
[
	{
		"id_mascota_encontrada":Integer,
		"id_mascota":Integer,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Agrega un objeto Mascota_encontrada a la tabla
`POST api/v1/mascota_encontrada/`

Campos del objeto:
```json
[
	{
		"id_mascota_encontrada":Integer,
		"id_mascota":Integer,
	}
]
```

**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


## Usuario

Detalles sobre la clase Usuario.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**

Retorna un objeto usuario dado un id.
`GET api/v1/usuario/id`

**respuesta:**
```json
[
	{
	        'correo_duenio':Email,
	        'nombre_duenio':String,
	        'pais':Sring,
	        'ciudad':String,
	        'colonia':String,
	        'calle':String,
	        'numero':String,
	}
]
```
- `404 Not Found` si el identificador no existe

Modifica los campos de un objeto usuario dado un id.
`PUT api/v1/usuario/id`

**Parametros**
```json
[
	{
	       'correo_duenio':Email,
	       'nombre_duenio':String,
	       'pais':Sring,
	       'ciudad':String,
	       'colonia':String,
	       'calle':String,
	       'numero':String,
	}
]
```
**respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto usuario de la tabla dado un id.
`DELETE api/v1/usuario/id`

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Crea un registro para un objeto usuario.
`POST api/v1/registro`

**Parametros**
```json
[
	{
		'correo_duenio':Email,
		'nombre_duenio':String,
		'pais':Sring,
		'ciudad':String,
		'colonia':String,
		'calle':String,
		'numero':String,
	}
]
```
**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente

Registra un usuario.
`POST api/v1/usuario`

**Parametros**
```json
[
	{
		'correo_duenio':Email,
		'nombre_duenio':String,
	}
]
```
**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


## Reporte

Detalles sobre la clase Reporte.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**

Retorna un objeto Reporte dado un id.
`GET api/v1/reporte/id`

```json
[
	{
		"id_reporte":Integer,
		"fecha_reporte":Date,
		"descripcion_reporte":String,
		"id_usuario":Integer,
		"id_mascota":Integer,
	}
]
```
- `404 Not Found` si el identificador no existe

Modifica los campos de un objeto dado un id.
`PUT api/v1/reporte/id`

**Parametros**
```json
[
	{
		"fecha_reporte":Date,
		"descripcion_reporte":String,
		"id_usuario":Integer,
		"id_mascota":Integer,
	}
]
```
**respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto dado un id.
`DELETE api/v1/reporte/id

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


Agregaun objeto Reporte a la tabla.
`POST api/v1/reporte/`

**Parametros**
```json
[
	{
		"fecha_reporte":Date,
		"descripcion_reporte":String,
		"id_usuario":Integer,
		"id_mascota":Integer,
	}
]
```
**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


Retorna todos los objetos en la tabla Reporte.`
`GET api/v1/reporte/`

**respuesta:**
```json
[
	{
		"id_reporte":Integer,
		"fecha_reporte":Date,
		"descripcion_reporte":String,
		"id_usuario":Integer,
		"id_mascota":Integer,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada



## Reporte avistado

Detalles sobre la clase Reporte_avistado.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**

Retorna un objeto Reporte_avistado dado un id.
`GET api/v1/reporte_avistado/id`

```json
[
	{
		"id_reporte_avistado":Integer,
		"lugar_avistado":String,
		"imagen_avistamiento":Image,
		"id_reporte":Integer,
	}
]
```
- `404 Not Found` si el identificador no existe

Modifica los campos de un objeto dado un id.
`PUT api/v1/reporte_avistado/id`

**Parametros**
```json
[
	{
		"lugar_avistado":String,
		"imagen_avistamiento":Image,
		"id_reporte":Integer,
	}
]
```
**respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto dado un id.
`DELETE api/v1/reporte_avistado/id

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


Agregaun objeto Reporte_avistado a la tabla.
`POST api/v1/reporte_avistado/`

**Parametros**
```json
[
	{
		"lugar_avistado":String,
		"imagen_avistamiento":Image,
		"id_reporte":Integer,
	}
]
```
**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


Retorna todos los objetos en la tabla Reporte_avistado.`
`GET api/v1/reporte_avistado/`

**respuesta:**
```json
[
	{
		"id_reporte_avistado":Integer,
		"lugar_avistado":String,
		"imagen_avistamiento":Image,
		"id_reporte":Integer,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


## Reporte encontrado

Detalles sobre la clase Reporte_encontrado.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**

Retorna un objeto Reporte_encontrado dado un id.
`GET api/v1/reporte_encontrado/id`

```json
[
	{
	    "id_reporte_encontrado":Integer,
	    "lugar_encontrado":String,
	    "imagen_encontrado":Image,
	    "mascota_recojida":String,
	    "id_reporte":Integer,
	}
]
```
- `404 Not Found` si el identificador no existe

Modifica los campos de un objeto dado un id.
`PUT api/v1/reporte_encontrado/id`

**Parametros**
```json
[
	{
	  "lugar_encontrado":String,
	  "imagen_encontrado":Image,
	  "mascota_recojida":String,
	}
]
```
**respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto dado un id.
`DELETE api/v1/reporte_encontrado/id

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


Agrega un objeto Reporte_encontrado a la tabla.
`POST api/v1/reporte_encontrado/`

**Parametros**
```json
[
	{
	  "lugar_encontrado":String,
	  "imagen_encontrado":Image,
	  "mascota_recojida":String,
	}
]
```
**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


Retorna todos los objetos en la tabla Reporte_encontrado.`
`GET api/v1/reporte_encontrado/`

**respuesta:**
```json
[
	{
	  "id_reporte_encontrado":Integer,
	  "lugar_encontrado":String,
	  "imagen_encontrado":Image,
	  "mascota_recojida":String,
	  "id_reporte":Integer,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


## Reporte perdido

Detalles sobre la clase Reporte_perdido.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Definiciones**

Retorna un objeto Reporte_perdido dado un id.
`GET api/v1/reporte_perdido/id`

```json
[
	{
	    "id_reporte_perdido":Integer,
	    "ultimo_lugar_visto":String,
	    "id_reporte":Integer,
	}
]
```
- `404 Not Found` si el identificador no existe

Modifica los campos de un objeto dado un id.
`PUT api/v1/reporte_perdido/id`

**Parametros**
```json
[
	{
	    "ultimo_lugar_visto":String,
	}
]
```
**respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto dado un id.
`DELETE api/v1/reporte_perdido/id

**respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


Agrega un objeto Reporte_perdido a la tabla.
`POST api/v1/reporte_perdido/`

**Parametros**
```json
[
	{
	    "id_reporte_perdido":Integer,
	    "ultimo_lugar_visto":String,
	    "id_reporte":Integer,
	}
]
```
**respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


Retorna todos los objetos en la tabla Reporte_perdido.`
`GET api/v1/reporte_perdido/`

**respuesta:**
```json
[
	{
	   "id_reporte_perdido":Integer,
	   "ultimo_lugar_visto":String,
	   "id_reporte":Integer,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

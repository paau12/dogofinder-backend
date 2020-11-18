# dogofinder-backend
DogoFinder Platform API


## Mascotas

### Detalles sobre la clase Mascota.

**Definición**

`GET api/v1/mascotas/id`

Retorna los campos de un objeto Mascota dado un id.

**Argumentos**
- `"id":int`	Identificador de objeto.

**Respuesta:**
- Si se encuentra un objeto con el id dado:
```json
[
    {
	"nombre_mascota":"string",
	"tipo_mascota":"string",
	"raza_mascota":"string",
	"descripcion_mascota":"string",
	"codigo_qr":"string",
	"foto_mascota":"url-imagen-perro",
	"in_home":true,
	"id_usuario": 5,
    }
]
```
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Elimina un objeto Mascota

**Definicion**

`DELETE api/v1/mascotas/id`

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Re-escribe los campos de un objeto mascota dado un id.

**Definición**

`PUT api/v1/mascotas/id`


**Parametros**
```json
[
    {
	"nombre_mascota":"string",
	"tipo_mascota":"string",
	"raza_mascota":"string",
	"descripcion_mascota":"string",
	"codigo_qr":"string",
	"foto_mascota":"url-imagen-perro",
	"in_home":true,
	"id_usuario": 5,
    }
]
```

**Respuesta:**
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Obtener todas las mascotas existentes

`GET api/v1/mascotas/`

**Respuesta:**
- Por cada mascota existente:
```json
[
    {
	"nombre_mascota":"string",
	"tipo_mascota":"string",
	"raza_mascota":"string",
	"descripcion_mascota":"string",
	"codigo_qr":"string",
	"foto_mascota":"url-imagen-perro",
	"in_home":true,
	"id_usuario": 5,
    },
    ...
]
```
- `400 Bad Request` si la petición esta mal formulada

### Inserta un nuevo objeto mascota a la tabla.

**Definición**

`POST api/v1/mascotas/`

Campos del objeto:
```json
[
    {
	"nombre_mascota":"string",
	"tipo_mascota":"string",
	"raza_mascota":"string",
	"descripcion_mascota":"string",
	"codigo_qr":"string",
	"foto_mascota":"url-imagen-perro",
	"in_home":true,
	"id_usuario": 5,
    },
]
```

**Respuesta:**
- `201 Created` si el objeto es almacenado correctamente
- `400 Bad Request` si la petición esta mal formulada


## Mascota Perdida

Detalles sobre la clase Mascota_perdida.

**Argumentos**
- `"id":int`	Identificador de objeto.

### Obtener las mascotas perdidas con su id

**Definición**

`GET api/v1/mascota_perdida/id`

**Respuesta:**
```json
[
	{
		"id_mascota_perdida":5,
		"id_mascota":5,
	}
]
```
- `404 Not Found` si el identificador no existe

### Modifica los campos de una mascota perdida

**Definición**

`PUT api/v1/mascota_perdida/id`

**Parametros**
```json
[
	{
		"id_mascota_perdida":5,
		"id_mascota":5,
	}
]
```

**Respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Elimina un objeto Mascota_perdida de la tabla

**Definición**

`DELETE api/v1/mascota_perdida/id`

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Retorna todas las mascotas perdidas en la tabla.

**Definición**

`GET api/v1/mascota_perdida/`

**Respuesta:**
```json
[
	{
		"id_mascota_perdida":5,
		"id_mascota":5,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Agrega un objeto Mascota_perdida a la tabla

**Definición**

`POST api/v1/mascota_perdida/`

Campos del objeto:
```json
[
	{
		"id_mascota_perdida":5,
		"id_mascota":5,
	}
]
```

**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


## Mascota Encontrada

### Obtener detalles sobre la mascota

**Definición**

`GET api/v1/mascota_encontrada/id`

**Argumentos**
- `"id":int`	Identificador de objeto.

**Respuesta:**
```json
[
	{
		"id_mascota_encontrada":5,
		"id_mascota":5,
	}
]
```
- `404 Not Found` si el identificador no existe

## Modificar los campos de una mascota encontrada con un id

**Definición**

`PUT api/v1/mascota_encontrada/<id>`

**Parametros**
```json
[
	{
		"id_mascota_encontrada":5,
		"id_mascota":5,
	}
]
```

**Respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


### Elimina un objeto Mascota_encontrada de la tabla

**Definición**

`DELETE api/v1/mascota_encontrada/id`

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Retorna todas las mascotas encontradas en la tabla.
`GET api/v1/mascota_encontrada/`

**Respuesta:**
```json
[
	{
		"id_mascota_encontrada":5,
		"id_mascota":5,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Agregar una mascota encontrada

**Definición**

`POST api/v1/mascota_encontrada/`

Campos del objeto:
```json
[
	{
		"id_mascota_encontrada":5,
		"id_mascota":5,
	}
]
```

**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


## Usuario

Detalles sobre la clase Usuario.

### Retorna un objeto usuario dado un id.

**Definiciones**

`GET api/v1/usuario/id`

**Argumentos**
- `"id":int`	Identificador de objeto.

**Respuesta:**
```json
[
	{
	        "correo_duenio":Email,
	        "nombre_duenio":"string",
	        "pais":Sring,
	        "ciudad":"string",
	        "colonia":"string",
	        "calle":"string",
	        "numero":"string",
	}
]
```
- `404 Not Found` si el identificador no existe

### Modificar los datos de un usuario con su id

**Definición**

`PUT api/v1/usuario/id`

**Parametros**
```json
[
	{
	       "correo_duenio":Email,
	       "nombre_duenio":"string",
	       "pais":Sring,
	       "ciudad":"string",
	       "colonia":"string",
	       "calle":"string",
	       "numero":"string",
	}
]
```
**Respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Elimina un objeto usuario de la tabla dado un id.

**Definición**

`DELETE api/v1/usuario/id`

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Crea un registro para un objeto usuario.

**Definición**

`POST api/v1/registro`

**Parametros**
```json
[
	{
		"correo_duenio":Email,
		"nombre_duenio":"string",
		"pais":Sring,
		"ciudad":"string",
		"colonia":"string",
		"calle":"string",
		"numero":"string",
	}
]
```
**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente

### Registra un usuario.

**Definición**

`POST api/v1/usuario`

**Parametros**
```json
[
	{
		"correo_duenio":Email,
		"nombre_duenio":"string",
	}
]
```
**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


## Reporte

Detalles sobre la clase Reporte.

**Argumentos**
- `"id":int`	Identificador de objeto.

### Retorna un objeto Reporte dado un id.

**Definición**

`GET api/v1/reporte/id`


```json
[
	{
		"id_reporte":5,
		"fecha_reporte":Date,
		"descripcion_reporte":"string",
		"id_usuario":5,
		"id_mascota":5,
	}
]
```
- `404 Not Found` si el identificador no existe

### Modifica los campos de un reporte con su id.

**Definición**

`PUT api/v1/reporte/id`

**Parametros**
```json
[
	{
		"fecha_reporte":Date,
		"descripcion_reporte":"string",
		"id_usuario":5,
		"id_mascota":5,
	}
]
```
**Respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Elimina un reporte con su id.

**Definición**

`DELETE api/v1/reporte/id

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


### Agrega un objeto Reporte a la tabla.

**Definición**

`POST api/v1/reporte/`

**Parametros**
```json
[
	{
		"fecha_reporte":Date,
		"descripcion_reporte":"string",
		"id_usuario":5,
		"id_mascota":5,
	}
]
```
**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente

### Retorna todos los objetos en la tabla Reporte.`

**Definición**

`GET api/v1/reporte/`

**Respuesta:**
```json
[
	{
		"id_reporte":5,
		"fecha_reporte":Date,
		"descripcion_reporte":"string",
		"id_usuario":5,
		"id_mascota":5,
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

### Retorna un objeto Reporte_avistado dado un id.

**Definición**

`GET api/v1/reporte_avistado/id`

```json
[
	{
		"id_reporte_avistado":5,
		"lugar_avistado":"string",
		"imagen_avistamiento":"url-imagen-perro",
		"id_reporte":5,
	}
]
```
- `404 Not Found` si el identificador no existe

### Modifica los campos de un objeto "reporte_avistado" con su id.

**Definición**

`PUT api/v1/reporte_avistado/id`

**Parametros**
```json
[
	{
		"lugar_avistado":"string",
		"imagen_avistamiento":"url-imagen-perro",
		"id_reporte":5,
	}
]
```
**Respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

Elimina un objeto dado un id.
`DELETE api/v1/reporte_avistado/id

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


### Agrega un objeto Reporte_avistado a la base de datos

**Definición**

`POST api/v1/reporte_avistado/`

**Parametros**
```json
[
	{
		"lugar_avistado":"string",
		"imagen_avistamiento":"url-imagen-perro",
		"id_reporte":5,
	}
]
```
**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente

### Obtener todos los reportes de los perritos avistados

**Definición**

`GET api/v1/reporte_avistado/`

**Respuesta:**
```json
[
	{
		"id_reporte_avistado":5,
		"lugar_avistado":"string",
		"imagen_avistamiento":"url-imagen-perro",
		"id_reporte":5,
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

### Retorna un objeto Reporte_encontrado dado un id.

**Definición**

`GET api/v1/reporte_encontrado/id`

```json
[
	{
	    "id_reporte_encontrado":5,
	    "lugar_encontrado":"string",
	    "imagen_encontrado":"url-imagen-perro",
	    "mascota_recojida":"string",
	    "id_reporte":5,
	}
]
```
- `404 Not Found` si el identificador no existe

### Modifica los campos de un "reporte avistado" con su id

**Definición**

`PUT api/v1/reporte_encontrado/id`

**Parametros**
```json
[
	{
	  "lugar_encontrado":"string",
	  "imagen_encontrado":"url-imagen-perro",
	  "mascota_recojida":"string",
	}
]
```
**Respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Elimina un reporte de un perrito avistado con su id

**Definición**

`DELETE api/v1/reporte_encontrado/id`

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


### Agrega un objeto Reporte_encontrado a la tabla.

**Definición**

`POST api/v1/reporte_encontrado/`

**Parametros**
```json
[
	{
	  "lugar_encontrado":"string",
	  "imagen_encontrado":"url-imagen-perro",
	  "mascota_recojida":"string",
	}
]
```
**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


### Retorna todos los objetos en la tabla Reporte_encontrado.

**Definición**

`GET api/v1/reporte_encontrado/`

**Respuesta:**
```json
[
	{
	  "id_reporte_encontrado":5,
	  "lugar_encontrado":"string",
	  "imagen_encontrado":"url-imagen-perro",
	  "mascota_recojida":"string",
	  "id_reporte":5,
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

### Obtener el reporte de un perrito perdido con su id.

**Definición**

`GET api/v1/reporte_perdido/id`

```json
[
	{
	    "id_reporte_perdido":5,
	    "ultimo_lugar_visto":"string",
	    "id_reporte":5,
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
	    "ultimo_lugar_visto":"string",
	}
]
```
**Respuesta:**

- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

### Elimina un objeto dado un id.

`DELETE api/v1/reporte_perdido/id`

**Respuesta:**
- `204 No Content` si el elemento se elimino correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada


### Agrega un perrito perdido a la base de datos

**Definición**

`POST api/v1/reporte_perdido/`

**Parametros**
```json
[
	{
	    "id_reporte_perdido":5,
	    "ultimo_lugar_visto":"string",
	    "id_reporte":5,
	}
]
```
**Respuesta:**
- `400 Bad Request` si la petición esta mal formulada
- `201 Created` si el objeto es almacenado correctamente


### Obtener todos los reportes de perritos perdidos

**Definición**

`GET api/v1/reporte_perdido/`

**Respuesta:**
```json
[
	{
	   "id_reporte_perdido":5,
	   "ultimo_lugar_visto":"string",
	   "id_reporte":5,
	},
	...
]
```
- `204 No Content` si el elemento se modifico correctamente
- `404 Not Found` si el identificador no existe
- `400 Bad Request` si la petición esta mal formulada

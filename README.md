# dogofinder-backend
DogoFinder Platform API - v1

## Endpoint

Todas las peticiones de la API tienen como base la siguiente URL
```url
http://dogofinder.herokuapp.com/api/v1/
```

## Autenticación

### Registro de usuarios

Los usuarios se pueden registrar con un nombre de usuario, un correo, y una contraseña. La contraseña debe ser validada dos veces para poder proceder.

**Definición**

`POST api/v1/auth/signup/`

**Argumentos**
- `"username":string`, nombre de usuario
- `"email":string`, correo electrónico del usuario
- `"password1":string`, contraseña deseada
- `"password2":string`, confirmación de contraseña deseada

**Respuesta**
- Si todos los campos son validados correctamente, se regresará un token de autenticación. 
- Este token debe ser almacenado en el front-end por localStorage o por cookies para la persistencia de sesión del usuario.
```json
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "key": "84321390802990df5ac0809c9066b3fcc3bee731"
}
```

- Si hay algún campo obligatorio faltante:

```json
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username": [
        "This field may not be blank."
    ],
    "password1": [
        "This field may not be blank."
    ],
    "password2": [
        "This field may not be blank."
    ]
}
```

### Iniciar sesión con una cuenta ya registrada

Una vez que el usuario está registrado, puede ingresar con su nombre de usuario y contraseña.

**Definición**

`POST /api/v1/auth/login/`

**Argumentos**
- `"username":string`, nombre de usuario
- `"password":string`, contraseña deseada

**Respuesta**
- Si todos los campos son validados correctamente, se regresará un token de autenticación.
- Este token debe ser almacenado en el front-end por localStorage o por cookies para la persistencia de sesión del usuario.
```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "key": "13336c24a8018955b74a058b5a43fa8e58a552cc"
}
```

- Si la contraseña es incorrecta:

```json
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

### Cerrar sesión de una cuenta activa

Para que el usuario cierre sesión de la cuenta activa, basta con hacer una petición GET.

**Definición**

`GET /api/v1/auth/logout/`

Esta petición no acepta ni regresa nada. Solo elimina el token del usuario con la cuenta activa.

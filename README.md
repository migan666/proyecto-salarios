# Proyecto Django: Gestión de Salarios

Este proyecto es una aplicación Django que gestiona la lista de salarios de empleados, permitiendo ver y añadir nuevos registros. Este README proporciona instrucciones detalladas para ejecutar el proyecto localmente, configurar la base de datos, y manejar migraciones, incluyendo la creación de un superusuario y la inserción automática de registros.

## Requisitos previos

Asegúrate de tener instalados los siguientes requisitos antes de empezar:

- Python 3.7+
- pip (gestor de paquetes de Python)
- MySQL (base de datos compatible)
- Django 3.2+ (ya incluido en el `requirements.txt`)

## Instrucciones para la configuración del proyecto localmente

### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/migan666/proyecto-salarios.git
cd proyecto-salarios
```

### 2. Instalar dependencias


```bash
pip install -r requirements.txt
```


### 3. Configurar la base de datos MySql en su ambiente local con los siguiente datos

```bash
NAME_DB_PRODUCTION=dbprueba
USER_DB_PRODUCTION=root
PASSWORD_DB_PRODUCTION=root
HOST_DB_PRODUCTION=localhost
PORT_DB_PRODUCTION=3306
```



### 3. Crear las migraciones

```bash
python manage.py makemigrations
```

### 4. Ejecutar las migraciones

```bash
python manage.py migrate
```


Durante este paso, se insertarán 5 registros automáticos en la tabla de salarios. Estos registros son:

Nombre: Juan, Edad: 25, Ciudad: Lima, Salario: 2500.50
Nombre: Pedro, Edad: 30, Ciudad: Trujillo, Salario: 3200.00
Nombre: Ana, Edad: 28, Ciudad: Lima, Salario: 2900.75
Nombre: Laura, Edad: 35, Ciudad: Chiclayo, Salario: 4000.00
Nombre: Carlos, Edad: 22, Ciudad: Piura, Salario: 1800.25


### 4. Ejecutar las migraciones

```bash
python manage.py migrate
```

### 5. Crear un superusuario

```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```



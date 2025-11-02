# TEST TECNICO SOFTWARE ENGINEER I

## Características
* Análisis de productos
* Búsqueda: Búsqueda de productos por nombre y palabras clave
* Sustitución: Recomendación de alternativas usando embeddings semánticos

## Stack Tecnológico

### Backend 
* Python
* FastAPI 
* SQLAlchemy
* Pydantic

### Base de Datos
* PostgreSQL 
* Adminer

### Otros
* Docker + Docker Compose

## Requisitos 
* Docker Desktop (Windows/Mac) o Docker Engine (Linux)
* Git

## Instalación y Ejecución

### 1. Instalar Docker
* **Windows**: [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)
* **Mac**: [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/)
* **Ubuntu/Linux**: [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)

#### Verificar instalación
```bash
docker --version
docker-compose --version
```

### 2. Clonar el repositorio
```bash
git clone git@github.com:Rociovenegas/green-retail.git
cd green-retail
```

### 3. Levantar los servicios
```bash
# Primera vez (construir imágenes)
docker-compose up --build

# Siguientes veces
docker-compose up

# Modo detached (en segundo plano)
docker-compose up -d
```

### 4. Verificar que todo funciona
Abre tu navegador en:
* **API Docs**: http://localhost:8000/docs
* **Adminer (BD)**: http://localhost:8080

### 5. Detener los servicios
```bash
# Detener contenedores
docker-compose down

# Detener y eliminar volúmenes
docker-compose down -v
```

##  Configuración

### Variables de Entorno
El proyecto usa las siguientes variables de entorno (configuradas en `docker-compose.yml`):
```yaml
# Base de Datos PostgreSQL
POSTGRES_USER=user1
POSTGRES_PASSWORD=123456
POSTGRES_DB=green-retail

# Backend FastAPI
DATABASE_URL=postgresql://user1:123456@db:5432/green-retail
```

### Acceso a Adminer (Administrador de BD)
1. Ir a http://localhost:8080
2. Usar estas credenciales:
   - **Sistema**: PostgreSQL
   - **Servidor**: db
   - **Usuario**: user1
   - **Contraseña**: 123456
   - **Base de datos**: green-retail

---

##  Algoritmos Implementados 




### 1. Sistema de Scoring de Sostenibilidad 

**Ubicación**: `backend/app/algorithms/scoring.py`

**Descripción**: Calcula un puntaje de sostenibilidad 


### 2. Algoritmo de Sustitución 

**Ubicación**: `backend/app/algorithms/substitution.py` y `embeddings.py`

**Descripción**: Encuentra productos sustitutos usando **embeddings semánticos** basados en el modelo `all-MiniLM-L6-v2` de Sentence Transformers.

**Proceso**:
1. **Generación de embeddings**:
   - Convierte el **nombre del producto original** en un vector
   - Convierte las **keywords de los productos** en vectores

2. **Cálculo de similitud coseno**:
   Retorna un valor entre 0 y 1 (1 = idéntico, 0 = totalmente diferente)

3. **Selección del mejor sustituto**:
   - Ordena candidatos por similitud
   - Excluye el producto original

---
**pd**: Estos algoritmos fueron implementados en su momento el día viernes, en un proyecto que era un solo main.py, muy posiblemente no puedan ser integrados en el tiempo límite.

## Endpoints API

### Productos

#### `GET /api/products/`
Obtiene todos los productos.

#### `GET /api/products/search?q={query}`
Busca productos por nombre o palabras clave.

#### `GET /api/products/{product_id}`
Obtiene un producto específico por ID.

### Tiendas

#### `GET /api/stores/`
Obtiene todos las tiendas.

#### `GET /api/stores/search?q={query}`
Busca tiendas por nombre o palabras clave.

#### `GET /api/stores/{store_id}`
Obtiene una tienda específico por ID.

---

## Uso de IA

Este proyecto fue desarrollado con asistencia de Claude para:

### Contexto
La candidata (yo) nunca había levantado un sistema desde cero. Se tenía experiencia utilizando algunas herramientas pero en casos aislados, y la experiencia en empleos reales fue en grandes empresas donde todo el sistema ya está en producción. Al momento de ver la prueba entendió que no podría terminar y el primer día lo dedicó a implementar algoritmos en ambientes muy controlados.

### Principales áreas de asistencia:

#### Diseño de Arquitectura
- Estructuración modular del código (routers, services, algorithms)

#### Configuración de Infraestructura
- Conexión entre servicios: base de datos y API

#### Documentación
- Corrección del README

#### Formateo de código
- Corrección mayormente en mezcla de inglés y español

#### Debugging y Resolución de Problemas
- El uso de la IA en este proyecto fue inversamente proporcional al tiempo restante para la entrega del mismo
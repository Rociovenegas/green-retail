FROM python:3.11-slim

WORKDIR /usr/src/backend

# Instalar dependencias del sistema necesarias para compilar
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    postgresql-client \
    libpq-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Actualizar pip
RUN pip install --upgrade pip

# Copiar requirements
COPY backend/requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY backend/ .

# Exponer puerto
EXPOSE 8000

# Comando para iniciar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
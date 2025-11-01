from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products


app = FastAPI(
    title="LiquiVerde API",
    description="API para retail inteligente y sostenible",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    products.router,
    prefix="/api/products",
    tags=["Products"]
)

@app.get("/")
def read_root():
    return {
        "message": "LiquiVerde API is running",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
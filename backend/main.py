from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI(title="API Immobilier", version="1.0.0")

# Autorise le frontend à appeler l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API Immobilier opérationnelle"}

@app.get("/data")
def get_data():
    """Renvoie les données du CSV"""
    df = pd.read_csv("data.csv")
    return {
        "columns": df.columns.tolist(),
        "rows": df.values.tolist(),
        "count": len(df)
    }

@app.get("/stats")
def get_stats():
    """Renvoie les statistiques"""
    df = pd.read_csv("data.csv")
    return {
        "mean_price": float(df['prix'].mean()),
        "mean_surface": float(df['surface'].mean()),
        "correlation": float(df['surface'].corr(df['prix']))
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
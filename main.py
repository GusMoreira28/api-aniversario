from fastapi import FastAPI
from db import get_connection
from fastapi.middleware.cors import CORSMiddleware # Importe o CORSMiddleware

app = FastAPI()


origins = [
    "http://172.16.0.25",  # A origem do seu frontend Next.js
    "http://intranet.funev.org.br",  # Outra forma comum de localhost
    "http://172.16.0.25:3000",  # Se você estiver usando React no localhost
    "http://localhost",    # útil para dev
    "http://localhost:3000",  # se usar React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Lista de origens que podem fazer requisições
    allow_credentials=True,         # Permitir cookies, cabeçalhos de autorização, etc.
    allow_methods=["*"],            # Permitir todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Permitir todos os cabeçalhos HTTP
)

@app.get("/colaborador")
def listar_colaborador():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT fun.nomfun 'nome',FORMAT(fun.datnas, 'dd/MM/yyyy') 'data' FROM r034fun fun WHERE fun.codfil = 2 AND fun.sitafa IN (1 , 2) AND fun.tipcol = 1 ORDER BY MONTH(fun.datnas) ASC, DAY(fun.datnas) ASC")
    rows = cursor.fetchall()
    usuarios = [{"nome": r.nome, "data": r.data } for r in rows]
    conn.close()
    return usuarios

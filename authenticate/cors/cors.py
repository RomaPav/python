from main import app
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:4200",
    "https://myfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

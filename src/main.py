from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from functools import lru_cache
import os

from routes import users, vendors, medicines, purchases, customers


app = FastAPI()


@lru_cache()
def cached_dotenv():
    load_dotenv()


cached_dotenv()


origins = [
    os.environ.get("URL_ONE"),
    os.environ.get("URL_TWO"),
    # os.environ.get("URL_THREE"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(medicines.router)
app.include_router(vendors.router)
app.include_router(purchases.router)
app.include_router(customers.router)

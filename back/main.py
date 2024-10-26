import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller.user_controller import router as user_api
from controller.coin_controller import router as coin_api
from controller.order_controller import router as order_api
from controller.trade_lot_controller import router as trade_route_api
from controller.bit_cintroller import router as bit_router_api

app = FastAPI()

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

app.include_router(user_api, prefix="/users")
app.include_router(coin_api, prefix="/coin")
app.include_router(order_api, prefix="/order")
app.include_router(trade_route_api, prefix="/trade-lot")
app.include_router(bit_router_api, prefix="/bit")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

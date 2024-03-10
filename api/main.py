from fastapi import FastAPI

from converter_api.routes import router

app = FastAPI(title="Teste das rotas")

app.include_router(router=router)

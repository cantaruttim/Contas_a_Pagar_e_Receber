import uvicorn
from fastapi import FastAPI
from contas_a_pagar_e_contas_a_receber.router import contas_a_pagar_e_contas_a_receber_routers
from shared.database import engine, Base
from contas_a_pagar_e_contas_a_receber.models.contas_a_pagar_e_contas_a_receber_model import ContaPagarReceber

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return "<h1>Home Page</h1>"


# incluimos essa nova rota no main
app.include_router(contas_a_pagar_e_contas_a_receber_routers.router)


if __name__ == "__main__":
    uvicorn.run(app)

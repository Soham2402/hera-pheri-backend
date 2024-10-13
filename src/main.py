import logging

from fastapi import FastAPI

from src.database import CLIENT, DB_NAME


async def db_lifespan(app: FastAPI):
    app.mongodb_client = CLIENT
    app.database = DB_NAME
    ping_response = await app.database.command("ping")
    if int(ping_response["ok"]) != 1:
        logging.error("Connection not setup")
        raise Exception("Problem connecting to database cluster.")
    else:
        logging.info("Connected to database cluster.")

    yield

    app.mongodb_client.close()

app = FastAPI(lifespan=db_lifespan)

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# from contextlib import asynccontextmanager, contextmanager

# from sqlalchemy import text
# from app.core.connect_db import create_connection
# from app.routes import add_user_route
# from app.models.user_details import Base


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     try:
#         engine = await create_connection()
#         Base.metadata.create_all(bind=engine)
#         with engine.connect() as conn:
#             conn.execute(text("SELECT 1"))
#             print("✅ Successfully connected to the database.")
#             print("Application Startup Complete")
#     except Exception as e:
#         print("Failed to start application: ", e)
#     yield
#     print("Application Closed Successfully")


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from contextlib import asynccontextmanager
from app.core.connect_db import async_engine
from app.models.user_details import Base
from sqlalchemy import text

from app.routes import add_user_route
from app.routes import user_login_route
from app.routes import message_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            await conn.execute(text("SELECT 1"))
        print("Application startup complete✅")
    except Exception as e:
        print("Failed to start application ",e)
    yield
    print("Application closed successfully")


app = FastAPI(lifespan=lifespan)


app.include_router(add_user_route.router)
app.include_router(user_login_route.router)
app.include_router(message_route.router)




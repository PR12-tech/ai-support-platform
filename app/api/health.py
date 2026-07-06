from fastapi import APIRouter, status
from sqlalchemy import text
from app.database.db import SessionLocal
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@router.get("/ready")
def readiness_check():
    db = SessionLocal()

    try:

        db.execute(text("SELECT 1"))

        return {
            "status": "ready",
            "database": "connected"
        }


    except SQLAlchemyError:

        return JSONResponse(

            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,

            content={

                "status": "not_ready",

                "database": "disconnected",

            },

        )
    finally:
        db.close()
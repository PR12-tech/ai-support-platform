from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.models.user import User
from app.database.db import get_db
from app.auth.security import hash_password
from app.schemas.user import UserLogin
from app.auth.security import verify_password
from app.auth.jwt_handler import create_access_token
from app.auth.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register")
def register(
        user: UserCreate,
        db: Session = Depends(get_db)
):
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not db_user:
        return{
            "message": "Invalid Credentials"
        }

    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        return {
            "message": "Invalid Credentials"
        }

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
        current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }
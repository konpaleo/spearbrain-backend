from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.core import security
from app.core.config import settings
from app.schemas.token import Token

router = APIRouter()


@router.post("/access-token", response_model=Token)
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    if (
        form_data.username != settings.DEMO_USER_EMAIL
        or form_data.password != settings.DEMO_USER_PASSWORD
    ):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = security.create_access_token(
        subject=form_data.username,
        expires_delta=access_token_expires,
    )
    return Token(access_token=token)

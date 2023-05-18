from fastapi import APIRouter, Depends, status, Response
from typing import Annotated
from app.features.classes import User

router = APIRouter(prefix="/users", tags=["users"])


users = []


@router.get("/{uuid}")
def get_user(uuid: int, res: Response):
    for user in users:
        if user.get_uuid() == uuid:
            return user.to_json()
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"No user matches id: {uuid}"}

@router.post("/")
def create_user(new_user: Annotated(User, Depends(User))):
    users.append(new_user)
    return { 'uuid': new_user.get_uuid() }
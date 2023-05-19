from fastapi import APIRouter, Depends, status, Response
from typing import Annotated
from app.features.classes import User
from app.database import connection
from psycopg2.errors import UniqueViolation

router = APIRouter(prefix="/users", tags=["users"])

keys = ['username', 'email', 'password', 'device_code']

@router.get("/{uuid}")
def get_user(uuid: int, res: Response):
    with connection.cursor() as db:
        query = f"SELECT * FROM users WHERE uuid = '{uuid}'"
        db.execute(query)
        row = db.fetchone()
        if row is None:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": f"No user matches id: {uuid}"}
        return {i: j for i, j in zip(keys, row[1:])}

@router.post("/")
def create_user(new_user: Annotated[User, Depends(User)], res: Response):
    with connection.cursor() as db:
        try:
            keys_post = f"{keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}"
            query = f"INSERT INTO users ({keys_post}) VALUES ({new_user.to_values()}) RETURNING *;"
            db.execute(query)
            row = db.fetchone()
            connection.commit()
            return { 'uuid': row[0] }
        except UniqueViolation:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {'error': f'User with email: {new_user.get_email()} already exists.'}

from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Example endpoint
@router.get("/")
def get_users():
    return {"message": "List of users"}
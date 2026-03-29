from fastapi import APIRouter
from pydantic import BaseModel
from app.services.query_service import process_query

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query")
def query_api(request: QueryRequest):
    response = process_query(request.query)
    return response
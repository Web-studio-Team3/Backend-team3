from fastapi import APIRouter, status, HTTPException

from app.infrastracture.es_connect import ES_Connect

router = APIRouter()


@router.get(path='/')
async def search(query: str):
    try:
        es = ES_Connect.connect()
        items = await es.search(
            index="items", 
            query={
                "match": {
                    "title": query
                }
            })
        # categories = await es.search(
        #     index=
        # )
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No items"
        )
    return items
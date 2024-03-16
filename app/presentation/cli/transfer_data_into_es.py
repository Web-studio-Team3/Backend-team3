import asyncio
from elasticsearch import AsyncElasticsearch
from app.core.item.entities.item import Item
from app.infrastracture.es_connect import ES_Connect
from app.infrastracture.connect import database

conn = ES_Connect.connect()
async def get_data() -> list[Item]:
    try:
        items = database["item"].find()
        if not items:
            raise TypeError
        items_res = [] 
        for item in items:
            items_res.append(
                Item(
                    id=str(item["_id"]),
                    category_id=str(item["category_id"]),
                    title=item["title"],
                    description=item["description"],
                    condition=item["condition"],
                    address=item["address"],
                    cost=item["cost"],
                    status=item["status"]
                )
            )
    except TypeError as e:
        return []
    return items_res

async def transfer_data_into_es(conn: AsyncElasticsearch):
    items = await get_data()
    for item in items:
        es_doc = {
            "category_id": item.category_id,
            "title": item.title,
            "description": item.description,
            "condition": item.condition,
            "address": item.address,
            "cost": item.cost,
            "status": item.status,
        }
        await conn.index(index="items", id=item.id, document=es_doc)
        await conn.close()

asyncio.run(transfer_data_into_es(conn))

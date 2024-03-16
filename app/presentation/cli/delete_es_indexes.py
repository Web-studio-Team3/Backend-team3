import asyncio
from elasticsearch import AsyncElasticsearch
from app.infrastracture.es_connect import ES_Connect

conn = ES_Connect.connect()

async def delete_indexes(conn: AsyncElasticsearch):
    await conn.options(ignore_status=[400,404]).indices.delete(index='items')

async def delete(conn: AsyncElasticsearch):
    await delete_indexes(conn)
    await conn.close()

asyncio.run(delete(conn))

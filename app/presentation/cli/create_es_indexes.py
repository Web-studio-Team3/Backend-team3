import asyncio
from elasticsearch import AsyncElasticsearch
from app.infrastracture.es_connect import ES_Connect

from .indexes.items import items_mapping, items_settings

conn = ES_Connect.connect()

async def mapping_doc(conn: AsyncElasticsearch):
    await conn.indices.create(index='items', settings=items_settings, mappings=items_mapping)

async def mapping(conn: AsyncElasticsearch):
    await mapping_doc(conn)
    await conn.close()

asyncio.run(mapping(conn))

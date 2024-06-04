import asyncio
import asyncpg
from db_work import (
    get_all_documents,
    get_document,
    insert_new_katalog,
    insert_new_document,
    get_katalog_info,
)
from quart import Quart, request
from quart_auth import basic_auth_required, QuartAuth
import secrets
import yaml

app = Quart(__name__)
app.config["QUART_AUTH_BASIC_USERNAME"] = "admin"
app.config["QUART_AUTH_BASIC_PASSWORD"] = "admin"
app.secret_key = secrets.token_urlsafe(16)

QuartAuth(app)


async def connection():
    conn = await asyncpg.connect(
        user="admin", password="admin", database="katalog", host="postgres", port=5432
    )
    return conn


@app.route("/", methods=["GET"])
async def all_info():
    conn = await connection()
    result = await get_all_documents(conn)
    return yaml.dump(result)


@app.route("/<path:path>", methods=["GET"])
async def document(path):
    conn = await connection()
    split_path = path.split("/")
    last_info = split_path[-1]
    last_info_split = last_info.split("=")
    if len(last_info_split) == 2 and last_info_split[0] == "document":
        document_name = last_info_split[1]
        result = await get_document(conn, path, document_name)
    else:
        result = await get_katalog_info(conn, path)
        result = yaml.dump(result)
    return result


@app.route("/", methods=["POST"])
@basic_auth_required()
async def insert_new_data():
    conn = await connection()
    data = await request.get_data()
    str_data = data.decode("utf-8")
    if str_data[0] != "[" and str_data[-1] != "]":
        return "wrong request"
    str_data = str_data[1:-1]
    split_data = str_data.split(",")
    if split_data[0] == "document" and len(split_data) == 6 and "" not in split_data:
        katalog_path = split_data[1]
        document_name = split_data[2]
        document_format = split_data[3]
        document_size = split_data[4]
        document_hash = split_data[5]
        result = await insert_new_document(
            conn,
            katalog_path,
            (document_name, document_format, document_size, document_hash),
        )
    elif split_data[0] == "katalog" and len(split_data) == 3 and "" not in split_data:
        katalog_path = split_data[1]
        new_katalog_name = split_data[2]
        result = await insert_new_katalog(conn, katalog_path, new_katalog_name)
    else:
        return "wrong request"
    return result


app.run(host="0.0.0.0")

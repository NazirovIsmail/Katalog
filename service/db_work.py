import asyncio


async def get_all_documents(conn):
    all_katalog_info = await conn.fetch("SELECT id,name,parent_id FROM katalog")
    all_documents = await conn.fetch(
        "SELECT id,name,format,size,hash,parent_katalog_id FROM documents"
    )
    katalogs = {}
    for katalog in all_katalog_info:
        id = katalog[0]
        name = katalog[1]
        parent_id = katalog[2]
        katalogs[id] = {"name": name, "parent_id": parent_id, "inside": []}
    for document in all_documents:
        id = document[0]
        name = document[1]
        format = document[2]
        size = document[3]
        hash = document[4]
        katalog_parent_id = document[5]
        katalogs[katalog_parent_id]["inside"].append(
            {"name": name, "format": format, "size": size, "hash": hash}
        )
    finish_katalog = []
    for id in katalogs:
        katalog = katalogs[id]
        parent_id = katalog["parent_id"]
        if parent_id == 0:
            continue
        katalogs[parent_id]["inside"].append(
            {"name": katalog["name"], "inside": katalog["inside"]}
        )
    for id in katalogs:
        katalog = katalogs[id]
        if katalog["parent_id"] == 0:
            finish_katalog.append(
                {"name": katalog["name"], "inside": katalog["inside"]}
            )
    return finish_katalog


async def get_document(conn, katalog_path, document_name):
    split_katalog_path = katalog_path.split("/")[:-1]
    parent_id = 0
    for katalog_name in split_katalog_path:
        values = await conn.fetch(
            """SELECT id FROM katalog where name='%s' and parent_id='%s' """
            % (katalog_name, parent_id)
        )
        if values == []:
            return "wrong path"
        parent_id = values[0][0]
    document_data = await conn.fetch(
        """SELECT name,format,size,hash FROM documents where name='%s' and parent_katalog_id='%s' """
        % (document_name, parent_id)
    )
    if len(document_data) == 0:
        return "Nothing found. Maybe wrong document name"
    document_info = {
        "name": document_data[0][0],
        "format": document_data[0][1],
        "size": document_data[0][2],
        "hash": document_data[0][3],
    }
    return document_info


async def get_katalog_info(conn, katalog_path):
    split_katalog_path = katalog_path.split("/")
    if split_katalog_path[-1] == "":
        split_katalog_path = split_katalog_path[:-1]
    cur_layer_info = await get_all_documents(conn)
    for katalog_name in split_katalog_path:
        flag = False
        new_layer = None
        for cur_layer_katalog in cur_layer_info:
            if cur_layer_katalog["name"] == katalog_name:
                new_layer = cur_layer_katalog["inside"]
                flag = True
        if flag == False:
            return "Wrong path"
        else:
            cur_layer_info = new_layer
    return cur_layer_info


async def insert_new_katalog(conn, katalog_path, new_katalog_name):
    split_katalog_path = katalog_path.split("/")
    parent_id = 0
    for katalog_name in split_katalog_path:
        values = await conn.fetch(
            """SELECT id FROM katalog where name='%s' and parent_id='%s' """
            % (katalog_name, parent_id)
        )
        if values == []:
            return "wrong path"
        parent_id = values[0][0]
    already_exist_katalog = await conn.fetch(
        """SELECT id FROM katalog where name='%s' and parent_id='%s' """
        % (new_katalog_name, parent_id)
    )
    if len(already_exist_katalog) > 0:
        return "already exist"
    a = await conn.execute(
        """INSERT INTO public.katalog(name, parent_id)
	        VALUES ('%s', '%s')"""
        % (new_katalog_name, parent_id)
    )
    return "done"


async def insert_new_document(conn, katalog_path, document_info):
    split_katalog_path = katalog_path.split("/")
    parent_id = 0
    document_name = document_info[0]
    document_format = document_info[1]
    document_size = document_info[2]
    document_hash = document_info[3]
    for katalog_name in split_katalog_path:
        values = await conn.fetch(
            """SELECT id FROM katalog where name='%s' and parent_id='%s' """
            % (katalog_name, parent_id)
        )
        if values == []:
            return "wrong path"
        parent_id = values[0][0]
    already_exist_document = await conn.fetch(
        """SELECT id FROM documents where name='%s' and parent_katalog_id='%s' """
        % (document_name, parent_id)
    )
    if len(already_exist_document) > 0:
        return "already exist"
    await conn.execute(
        """INSERT INTO documents(
            name, format, size, hash, parent_katalog_id
            ) VALUES ('%s', '%s', '%s','%s','%s')"""
        % (document_name, document_format, document_size, document_hash, parent_id)
    )
    return "done"

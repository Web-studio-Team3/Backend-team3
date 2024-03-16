def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
        "password": item["password"],
        "fullname": item["fullname"],
        "date_of_birth": item["date_of_birth"]
        if "date_of_birth" in item.keys()
        else None,
        "photo_url": str(item["photo_url"]),
    }
    # if "date_of_birth" in item.keys():
    #     entity["date_of_birth"] = item["date_of_birth"]


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

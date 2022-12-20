def get_info_dict(info, meta):
    return {
        "message": info,
        "id": meta["id"],
        "name": meta["name"]
    }

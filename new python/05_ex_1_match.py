def http_status(status):
    match status:
        case _ if status > 500:
            return "internal server error"
        case _ if status > 400:
            return "not found"
        case _ if status > 200:
            return "ok"
        case _:
            return "unknown status"

print(http_status(400))
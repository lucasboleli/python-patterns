import os
from typing import Any, Protocol

from json_storage import JsonStorage
from mongo import MongoStorage
from s3 import S3Storage


# Protocol  <<<<===== Qualquer classe que implementa o metodo pode ser chamada


class DataPut(Protocol):
    def put(self, key: str, value: Any) -> None: ...


class DataGet(Protocol):
    def get(self, key: str) -> Any: ...


def pipeline(data_get: DataGet, data_put: DataPut, source_key: str) -> str:
    value = data_get.get(source_key)
    sink_key = f"{source_key}-out"

    # Do some processing on the value...
    value.update({"processed": True})

    data_put.put(sink_key, value)
    return sink_key


if __name__ == "__main__":
    in_key = "my-pipeline"

    # Ignore me :)
    os.environ["S3_CREDENTIALS_FILE"] = "s3-credentials.json"
    os.environ["MONGO_USERNAME"] = "isaac"
    os.environ["MONGO_PASSWORD"] = "password"

    print("====== s3 ======")
    s3_storage = S3Storage(os.environ["S3_CREDENTIALS_FILE"])
    out_key = pipeline(s3_storage, s3_storage, in_key)
    print(f"out_key: {out_key}")

    print("\n\n====== mongo ======")
    mongo_storage = MongoStorage(
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
    )
    out_key = pipeline(mongo_storage, mongo_storage, in_key)
    print(f"out_key: {out_key}")

    print("\n\n====== json ======")
    json_storage = JsonStorage("data.json")
    out_key = pipeline(json_storage, json_storage, in_key)
    print(f"out_key: {out_key}")

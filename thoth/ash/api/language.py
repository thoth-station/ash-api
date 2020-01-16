import os
from thoth.storages import CephStore


# Access points should be read in from .env file
store = CephStore(prefix=os.environ['THOTH_VECTOR_DATA_CEPH_BUCKET_PREFIX'])
store.connect()
store.check_connection()


def get(token):
    return {
            'token': token,
            'is_connected': store.is_connected(),
            'connection_tes': store.key_id,
        }, 200

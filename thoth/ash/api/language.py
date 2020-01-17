import os
from thoth.storages import CephStore


# Access points should be read in from .env file
store = CephStore(prefix=os.environ['THOTH_VECTOR_DATA_CEPH_BUCKET_PREFIX'])
store.connect()


def get(token):
    return {
            'token': token,
            'is_connected': store.is_connected(),
            'connection_alive': store.check_connection(),
        }, 200

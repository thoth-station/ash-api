import os
from typing import List
from thoth.storages import CephStore


store = CephStore(prefix='data/thoth/ash-api/ETM/words')
store.connect()


def retrieve_n_most_similar(token, n) -> List:
    if not store.document_exists(token):
        return {'error': f'The token: {token} is not in the vocabulary.'}, 404

    token_dict = store.retrieve_document(token)
    return [t for t in token_dict['most_similar'][:n]]


def get(token):
    """ Retrieves the 25 most similar tokens to {token} path param """
    return {
            'token': token,
            'most-similar-tokens': retrieve_n_most_similar(token, n=25),
        }, 200

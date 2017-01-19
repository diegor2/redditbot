from collections import defaultdict
from inspect import getmodule

import clients.abc


"""
    keep global bot instancies
"""
CLIENTS = defaultdict()

"""
    Register a client instance.
"""
def register(client_type, instance):
    if getmodule(client_type) != clients.abc:
        raise TypeError('Unsupported client type. '
                        'Must use a class from clients.abc module.')
    if not isinstance(instance, client_type):
        raise TypeError('Client instance should be of type '
                        + client_type.__name__)

    CLIENTS[client_type] = instance

"""
    Get a previous registered client.

    @return None if the name was not found.
"""
def get(name):
    return CLIENTS[client_type]

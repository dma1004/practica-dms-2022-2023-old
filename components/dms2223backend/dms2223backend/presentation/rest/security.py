import sys
from typing import Dict

import requests
from connexion.exceptions import Unauthorized
from flask import current_app

from dms2223backend.data.config import BackendConfiguration


def verify_api_key(token: str) -> Dict:
    """Callback testing the received API key.

    Args:
        - token (str): The received API key.

    Raises:
        - Unauthorized: When the given API key is not valid.

    Returns:
        - Dict: Information retrieved from the key to be passed to the endpoints.
    """
    with current_app.app_context():
        cfg: BackendConfiguration = current_app.cfg
        if token not in cfg.get_authorized_api_keys():
            raise Unauthorized('Invalid API key')
    return {}


def verify_token(token: str) -> Dict:
    auth_service_cfg = current_app.cfg.get_auth_service()
    base_url = f'http://{auth_service_cfg["host"]}:{auth_service_cfg["port"]}/api/v1'

    response: requests.Response = requests.get(
        base_url + f'/auth',
        headers={
            'Authorization': f'Bearer {token}',
            'X-ApiKey-Auth': auth_service_cfg['apikey_secret']
        },
        timeout=60
    )

    if not response.ok:
        raise Unauthorized("Invalid user token")

    return response.json()

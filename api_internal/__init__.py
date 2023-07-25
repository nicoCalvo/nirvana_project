"""
Entrypoint for module calling external apis.

Only one method exposed as the engine is handled in an asyncio loop within a Thread to
make as many calls as desired at the same time without coupling the logic with the external api

"""
from .deductible_api import (
    API_URLS,
    deducible_api_caller,
    DeductibleApiError,
    start_loop
)
__all__ = [
    'API_URLS',
    'deducible_api_caller',
    'DeductibleApiError'
    'start_loop',
]
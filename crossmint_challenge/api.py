import requests


class MegaverseAdapter:
    """
    API adapter used to communicate with the challenge API.

    Args:
        candidateId (str): Required candidate ID for API interactions.
    """

    def __init__(self, candidateId: str):
        self.base_uri: str = "https://challenge.crossmint.com"
        self.candidateId: str = candidateId

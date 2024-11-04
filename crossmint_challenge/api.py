from typing import Dict, List, Optional, Union
import requests

from crossmint_challenge.models import POLYanet, SOLoon, ComETH


class MegaverseAdapter:
    """
    API adapter used to communicate with the challenge API.

    Args:
        candidate_id (str): Required candidate ID for API interactions.
    """

    def __init__(self, candidate_id: str, uri: str = "https://challenge.crossmint.com"):
        self.base_uri: str = uri
        self.api:  str = f"{self.base_uri}/api"
        self.headers: Dict[str, str] = {"content-type": "application/json"}
        self.candidate_id: str = candidate_id
        self.megaverse: List[List[Optional[Dict[str, int]]]] = [[]]

    def fetch_map(self) -> List[List[Optional[Dict[str, int]]]]:
        megaverse = [[]]
        try:
            req = requests.get(
                f"{self.api}/map/{self.candidate_id}", headers=self.headers)

            if req.status_code not in [200]:
                req.raise_for_status()

            megaverse = req.json()["map"]["content"]
        except:
            print("Unable to load megaverse from candidate")

        return megaverse
    
    def fetch_goal(self) -> List[List[Optional[Dict[str, int]]]]:
        megaverse = [[]]
        try:
            req = requests.get(
                f"{self.api}/map/{self.candidate_id}/goal", headers=self.headers)

            if req.status_code not in [200]:
                req.raise_for_status()

            megaverse = req.json()["goal"]
        except:
            print("Unable to load megaverse goal from candidate")

        return megaverse

    def insert_astral_object(self, obj: Union[POLYanet, SOLoon, ComETH, object]) -> Dict[str, bool]:
        response: Dict[str, bool] = {"success": False}
        endpoint: Union[str, None] = None

        if isinstance(obj, POLYanet):
            endpoint = "polyanets"
        elif isinstance(obj, SOLoon):
            endpoint = "soloons"
        elif isinstance(obj, ComETH):
            endpoint = "comeths"
        else:
            raise TypeError("This is not a valid object.")

        try:
            req = requests.post(f"{self.api}/{endpoint}", headers=self.headers, json={
                **obj.__dict__, "candidateId": self.candidate_id})

            if req not in [200, 201]:
                req.raise_for_status()
        except Exception as e:
            print(e)
            print("Failed to insert astral object.")
            return response

        response["success"] = True
        return response

    def delete_astral_object(self, obj: Union[POLYanet, SOLoon, ComETH, object]) -> Dict[str, bool]:
        response: Dict[str, bool] = {"success": False}
        endpoint: Union[str, None] = None

        if isinstance(obj, POLYanet):
            endpoint = "polyanets"
        elif isinstance(obj, SOLoon):
            endpoint = "soloons"
        elif isinstance(obj, ComETH):
            endpoint = "comeths"
        else:
            raise TypeError("This is not a valid object.")

        try:
            req = requests.delete(f"{self.api}/{endpoint}", headers=self.headers, json={
                **obj.__dict__, "candidateId": self.candidate_id})

            if req not in [200, 201]:
                req.raise_for_status()
        except Exception as e:
            print(e)
            print("Failed to insert astral object.")
            return response

        response["success"] = True
        return response

import json
import time
import os

from dotenv import load_dotenv
from crossmint_challenge.models import POLYanet
from crossmint_challenge.api import MegaverseAdapter


load_dotenv()
candidate_id = os.getenv("CANDIDATE_ID")

adapter = MegaverseAdapter(candidate_id)

data = None

with open("./seeds/phase1.json") as f:
    data = json.loads(f.read())

for obj in data:
    poly = POLYanet(**obj)  # Create a model instance.
    
    time.sleep(2)  # It avoids 429 Too Many Requests Http error.

    # http POST request to set the object into the megaverse.
    adapter.insert_astral_object(poly)

# Sets the phase1 challenge (X shape) megaverse to the adapter
adapter.megaverse = adapter.fetch_map()

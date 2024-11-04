import time
import os

from dotenv import load_dotenv
from crossmint_challenge.models import ComETH, POLYanet, SOLoon
from crossmint_challenge.api import MegaverseAdapter


load_dotenv()
candidate_id = os.getenv("CANDIDATE_ID")

adapter = MegaverseAdapter(candidate_id)

data = adapter.fetch_goal()

for row_idx in range(len(data)):
    for col_idx in range(len(data[row_idx])):
        astral_obj = None
        if "POLYANET" in data[row_idx][col_idx]:
            astral_obj = POLYanet(row=row_idx, column=col_idx)  # Create a model instance.
        elif "SOLOON" in data[row_idx][col_idx] :
            color: str = data[row_idx][col_idx].split("_")[0]
            astral_obj = SOLoon(row=row_idx, column=col_idx, color=color.lower())
        elif "COMETH" in data[row_idx][col_idx] :
            direction: str = data[row_idx][col_idx].split("_")[0]
            astral_obj = ComETH(row=row_idx, column=col_idx, direction=direction.lower())

        # http POST request to set the object into the megaverse.
        if astral_obj:
            time.sleep(3)  # It avoids 429 Too Many Requests Http error.
            adapter.insert_astral_object(astral_obj)

# Sets the phase2 challenge (Logo shape) megaverse to the adapter
adapter.megaverse = adapter.fetch_map()

print(adapter.megaverse)
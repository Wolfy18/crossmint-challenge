# Crossmint Challenge

Welcome to our Crossmint coding challenge, in which you will help us mint a new megaverse into existence!

Megaverses are 2D spaces comprised of combinations of different astral objects: 🪐POLYanets with 🌙SOLoons around them and ☄comETHs floating around.

Your job as the master of the megaverse will be to create one with some given parameters and shapes. You will use a megaverse creator API to help you with such legendary quest.

The challenge is composed of 2 phases. In the first one you will learn how to interact with the API and create some 🪐POLYanets and validate them. In the second one you will create a bigger megaverse with some peculiar shape.

## Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To install the project, you need to have Poetry installed on your local machine. Poetry is a package manager for Python that makes it easy to manage project dependencies. Here's how to install Poetry on Linux Ubuntu:

```
curl -sSL https://install.python-poetry.org | python3 -
```

Once installed, you can verify Poetry is working by running:

```
poetry --version
```

### Installing the Project with Poetry

To install the project using Poetry, follow these steps:

**Step 1: Clone the Repository**

Clone the project repository to your local machine using Git:
```
git clone https://github.com/Wolfy18/crossmint-challenge.git
```

**Step 2: Navigate to the Project Directory**

Change into the project directory:
```
cd crossmint-challenge
```

**Step 3: Install Project Dependencies**

Use Poetry to install the project dependencies:
```
poetry install
```

## Usage <a name = "usage"></a>

To run the script, first start the Poetry shell by executing the following command:
```
poetry shell
```
Once in the Poetry shell, run 

```
python ./phase1.py
```

### Sample case

Sample case to insert one POLYanet

```python

import json
import time

from crossmint_challenge.models import POLYanet
from crossmint_challenge.api import MegaverseAdapter

adapter = MegaverseAdapter("candidate_id")

poly = POLYanet({"row": 0, "column": 0}) # Create model instance

adapter.insert_astral_object(poly) # http POST request to set the object into the megaverse.

adapter.megaverse = adapter.fetch_map() # Sets the phase1 challenge (X shape) megaverse to the adapter

```

### Tests

Use Poetry to run the tests by executing the following command:

```
poetry run python -m unittest discover -s tests -v
```

This command will discover and run all tests located in the `tests` directory.



import json
import urllib
import sys
import textwrap
import time
from typing import cast, Dict, Optional

import looker_sdk
from looker_sdk import models

# initiating Looker SDK 
sdk = looker_sdk.init31(config_file="looker.ini", section="Looker")

# testing if the API works
my_user = sdk.me()
print(my_user.first_name)

# updating the dashboard number with slug
response = sdk.update_dashboard(
    dashboard_id="201",
    body=models.WriteDashboard(
        title="Business Pulse (API Update)",
        slug="thisismynewdashslug123"
    ))
    

# confirming if it worked
response = sdk.dashboard(
    dashboard_id="201",
    fields="slug")
print(response)

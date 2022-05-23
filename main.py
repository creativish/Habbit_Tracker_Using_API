import requests
from datetime import datetime

TOKEN = "vishalpr234atapsi2ngh"
USER_NAME = "vishalll"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "vishal012345"


user_param = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# respo = requests.post(url=pixela_endpoint, json=user_param)
# print(respo.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_param = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# respo = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
# print(respo.text)

pixel_data_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))

pixel_param = {
    "date": DATE,
    "quantity": input("How many KiloMeters did you run today?"),
}


respo = requests.post(url=pixel_data_endpoint, json=pixel_param, headers=headers)
print(respo.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"

pixel_update_param = {
    "quantity": "7.8"
}

# respo = requests.put(url=pixel_update_endpoint,json=pixel_update_param, headers=headers)
# print(respo.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"

# respo = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(respo.text)
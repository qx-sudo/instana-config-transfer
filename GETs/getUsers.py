from dotenv import load_dotenv
import requests
import urllib3
import json
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
api_token = os.getenv("API_TOKEN_EXPORT")

instana_base_url = os.getenv("INSTANA_BASE_URL_EXPORT")
url = f"{instana_base_url}/api/settings/users"

headers = {
    "Authorization": f"apiToken {api_token}",
    "Accept": "application/json",
}

# GET
response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    os.makedirs("Instana", exist_ok=True)
    file_path = os.path.join("Instana", f"Users.json")
    with open(file_path, "w") as json_file:
        json.dump(response.json(), json_file, indent=4)
    print(f"✅ La respuesta se ha guardado correctamente en '{file_path}'.")
    
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    total=0
    for i, data in enumerate(data, start=1):
        total+=1
        if data.get('email') == "admin@instana.local":
            continue
        print(f"{data.get('email')}")
    print(f"\n✅ Total: {total} users")
else:
    print(f"❌ Error al obtener Users: {response.status_code}")
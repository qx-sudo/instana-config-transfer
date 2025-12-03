from dotenv import load_dotenv
import requests
import urllib3
import json
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
api_token = os.getenv("API_TOKEN_IMPORT")

instana_base_url = os.getenv("INSTANA_BASE_URL_IMPORT")
url = f"{instana_base_url}/api/events/settings/application-alert-configs"

headers = {
    "Authorization": f"apiToken {api_token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

file_path = "Instana/AppSmartAlerts_updated.json"
with open(file_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    
# POST
for i, data in enumerate(data, start=1):
    print(f"📤 Enviando Smart Alert {i}: {data.get('name')}")
    
    response = requests.post(url, headers=headers, json=data, verify=False)

    if response.status_code == 200:
        print(f"✅ Smart Alert {i} creada correctamente.")
    else:
        print(f"❌ Error en Smart Alert {i} (Código {response.status_code}): {response.text}")

print("🚀 Proceso completado.")
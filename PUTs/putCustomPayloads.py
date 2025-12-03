from dotenv import load_dotenv
import requests
import urllib3
import json
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
api_token = os.getenv("API_TOKEN_IMPORT")

instana_base_url = os.getenv("INSTANA_BASE_URL_IMPORT")
url = f"{instana_base_url}/api/events/settings/custom-payload-configurations"

headers = {
    "Authorization": f"apiToken {api_token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

file_path = "Instana/CustomPayloads.json"
with open(file_path, "r") as json_file:
    data = json.load(json_file)
    
# PUT
print(f"📤 Enviando CustomPayload")

response = requests.put(url, headers=headers, json=data, verify=False)

if response.status_code == 200:
    print(f"✅ Custom Payload creada correctamente.")
else:
    print(f"❌ Error en Custom Payload (Código {response.status_code}): {response.text}")

print("🚀 Proceso completado.")
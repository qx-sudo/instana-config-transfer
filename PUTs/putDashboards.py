from dotenv import load_dotenv
import requests
import urllib3
import json
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
api_token = os.getenv("API_TOKEN_IMPORT")

instana_base_url = os.getenv("INSTANA_BASE_URL_IMPORT")

headers = {
    "Authorization": f"apiToken {api_token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

file_path = "Instana/DashboardsList.json"
with open(file_path, "r") as json_file:
    data = json.load(json_file)
    
# PUT
for i, data in enumerate(data, start=1):
    print(f"📤 Enviando dashboard {i}: {data.get('title')}")
    url = f"{instana_base_url}/api/custom-dashboard/{data.get('id')}"
    
    with open(f"Instana/Dashboards/Dashboard_{i}.json", "r", encoding="utf-8") as json_file:
        dashboard = json.load(json_file)
    
    response = requests.put(url, headers=headers, json=dashboard, verify=False)

    if response.status_code == 200:
        print(f"✅ Dashboard {data.get('title')} creada correctamente.")
    else:
        print(f"❌ Error en dashboard {data.get('title')} (Código {response.status_code}): {response.text}")

print("🚀 Proceso completado.")
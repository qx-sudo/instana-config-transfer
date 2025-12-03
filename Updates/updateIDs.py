import json

# Rutas de los archivos
file_A = "Instana/AppSettings.json"
file_B = "Instana/AppSettings_new.json"
file_C1 = "Instana/AppSmartAlerts.json"
file_C2 = "Instana/GlobalSmartAlerts.json"

file_out_C1 = "Instana/AppSmartAlerts_updated.json"
file_out_C2 = "Instana/GlobalSmartAlerts_updated.json"

# --- Paso 1: cargar JSONs ---
with open(file_A, "r", encoding="utf-8") as f:
    json_A = json.load(f)

with open(file_B, "r", encoding="utf-8") as f:
    json_B = json.load(f)

with open(file_C1, "r", encoding="utf-8") as f:
    json_C1 = json.load(f)

with open(file_C2, "r", encoding="utf-8") as f:
    json_C2 = json.load(f)

# --- Paso 2: construir mapa id_A -> id_B usando "label" ---
map_A = {item["label"]: item["id"] for item in json_A}
map_B = {item["label"]: item["id"] for item in json_B}

id_map = {}
for label, id_A in map_A.items():
    if label in map_B:
        id_map[id_A] = map_B[label]

# --- Paso 3: función recursiva para reemplazar en cualquier JSON ---
def reemplazar_ids(data, mapping):
    if isinstance(data, dict):
        nuevo_dict = {}
        for k, v in data.items():
            new_key = mapping.get(k, k)  # reemplazo en key
            nuevo_dict[new_key] = reemplazar_ids(v, mapping)  # recursión en value
        return nuevo_dict
    elif isinstance(data, list):
        return [reemplazar_ids(i, mapping) for i in data]
    elif isinstance(data, str):
        return mapping.get(data, data)  # reemplazo en value
    else:
        return data

# --- Paso 4: aplicar reemplazo en los dos JSON destino ---
json_C1_modificado = reemplazar_ids(json_C1, id_map)
json_C2_modificado = reemplazar_ids(json_C2, id_map)

# --- Paso 5: guardar resultados ---
with open(file_out_C1, "w", encoding="utf-8") as f:
    json.dump(json_C1_modificado, f, indent=4, ensure_ascii=False)

with open(file_out_C2, "w", encoding="utf-8") as f:
    json.dump(json_C2_modificado, f, indent=4, ensure_ascii=False)

# --- Paso 6: log de cambios ---
print("✅ Reemplazos realizados:")
for id_a, id_b in id_map.items():
    print(f"  {id_a}  →  {id_b}")

print(f"\n📂 Archivos actualizados guardados en:\n - {file_out_C1}\n - {file_out_C2}")
print("🚀 Proceso completado.")
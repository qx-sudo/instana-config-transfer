import os
import json

# === RUTAS ===
USER_FILE = "Instana/Users.json"
DASHBOARD_DIR = "Instana/Dashboards"


def obtener_user_id(user_file):
    """Lee el ID del archivo user.json"""
    try:
        with open(user_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # user.json puede ser lista o dict
        if isinstance(data, list) and data:
            return data[0].get("id")
        elif isinstance(data, dict):
            return data.get("id")
        else:
            raise ValueError("Formato inesperado en user.json")

    except Exception as e:
        raise RuntimeError(f"Error leyendo {user_file}: {e}")


def actualizar_dashboard(path_archivo, nuevo_id):
    """Reemplaza los relatedId de relationType=USER en un dashboard"""
    try:
        with open(path_archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        modificado = False

        if "accessRules" in data and isinstance(data["accessRules"], list):
            for regla in data["accessRules"]:
                if regla.get("relationType") == "USER":
                    if regla.get("relatedId") != nuevo_id:
                        regla["relatedId"] = nuevo_id
                        modificado = True

        if modificado:
            with open(path_archivo, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"✅ Actualizado: {path_archivo}")
        else:
            print(f"➡️  Sin cambios: {path_archivo}")

    except Exception as e:
        print(f"❌ Error procesando {path_archivo}: {e}")


def main():
    nuevo_id = obtener_user_id(USER_FILE)
    print(f"🔑 ID obtenido de user.json: {nuevo_id}")

    for archivo in os.listdir(DASHBOARD_DIR):
        if archivo.endswith(".json"):
            ruta = os.path.join(DASHBOARD_DIR, archivo)
            actualizar_dashboard(ruta, nuevo_id)


if __name__ == "__main__":
    main()

# instana-config-transfer
Instana Configuration Exporter/Importer

Herramienta en Python para exportar e importar configuraciones de Instana entre entornos. Los scripts obtienen la configuración desde una instancia origen (export) y la aplican en una instancia destino (import) mediante las APIs de Instana.

## Requisitos
- Python 3.9 o superior
- Dependencias: `requests`, `python-dotenv`, `urllib3`

Instala las dependencias con:

```bash
pip install requests python-dotenv urllib3
```

## Variables de entorno
Crea un archivo `.env` en la raíz del proyecto con las credenciales de ambos entornos:

```bash
API_TOKEN_EXPORT='your_source_api_token'
INSTANA_BASE_URL_EXPORT='https://your_source-unit-name.instana.io'

API_TOKEN_IMPORT='your_destination_api_token'
INSTANA_BASE_URL_IMPORT='https://your_destination-unit-name.instana.io'
```

- Las variables `*_EXPORT` se usan al obtener configuraciones.
- Las variables `*_IMPORT` se usan al aplicar configuraciones en el entorno destino.

## Exportar configuraciones
El proceso descarga dashboards, alertas, servicios y otros recursos a la carpeta `Instana/`.

```bash
python export_config.py
```

El flujo ejecuta una lista de scripts en `GETs/`, que primero generan `Instana/DashboardsList.json` y luego descargan los recursos individuales en subcarpetas, por ejemplo `Instana/Dashboards/` y `Instana/AlertChannels.json`.

## Importar configuraciones
Para aplicar la configuración en el entorno destino, utiliza:

```bash
python import_config.py
```

Este comando ejecuta secuencialmente los scripts de `PUTs/`, `POSTs/` y `Updates/`, enviando los archivos generados en la carpeta `Instana/` hacia la instancia destino. Cada script muestra en consola el recurso que está procesando y el resultado de la llamada API.

## Notas
- Los scripts deshabilitan las advertencias de certificado (`urllib3.disable_warnings`) al usar `verify=False` en las solicitudes HTTPS.
- Asegúrate de que la carpeta `Instana/` contenga los archivos exportados antes de iniciar la importación.
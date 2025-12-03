import subprocess

scripts = [
    "PUTs/putAlertChannels.py",
    "PUTs/putServices.py",
    "PUTs/putCustomPayloads.py",
    "POSTs/postAppSettings.py",
    "Updates/getAppSettings.py",
    "Updates/updateIDs.py",
    "POSTs/postAppSmartAlert.py",
    "POSTs/postGlobalSmartAlert.py",
    "POSTs/postCustomEvents.py",
    "PUTs/putAlerts.py",
    "Updates/getUsers.py",
    "Updates/updateDashboards.py",
    "PUTs/putDashboards.py",
    "PUTs/putMaintenance.py"
]

for script in scripts:
    print(f"Ejecutando {script}...")
    result = subprocess.run(["python", script])

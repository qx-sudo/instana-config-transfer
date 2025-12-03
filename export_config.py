import subprocess

scripts = [
    "GETs/getDashboards.py",
    "GETs/getAlertChannels.py",
    "GETs/getAlerts.py",
    "GETs/getAppSettings.py",
    "GETs/getAppSmartAlert.py",
    "GETs/getCustomEvents.py",
    "GETs/getCustomPayloads.py",
    "GETs/getGlobalSmartAlert.py",
    "GETs/getMaintenance.py",
    "GETs/getServices.py"
]

subprocess.run(["python", "GETs/getDashboardsList.py"])

processes = [subprocess.Popen(["python", script]) for script in scripts]

for process in processes:
    process.wait()

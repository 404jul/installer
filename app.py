import os
import shutil
import sys, json
import os, subprocess
MODS=[os.path.join(sys._MEIPASS, 'mods', x) for x in os.listdir(os.path.join(sys._MEIPASS, 'mods'))]
MINECRAFT_DIR = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft")
LAUNCHER_PROFILES = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft", "launcher_profiles.json")
FABRIC_INSTALLER = os.path.join(sys._MEIPASS, 'fabric-installer-1.0.0.exe')
FABRIC_VERSION = "0.15.6"
PROFILE_TOKEN = None

profile = {
    "name": "Voice-Chat-Modpack",
    "type": "custom",
    "javaArgs": "-Xmx2G",
    "icon": "Grass",
    "lastVersionId": f'fabric-loader-{FABRIC_VERSION}-1.20.4',
}

def get_minecraft_profiles():
    with open(LAUNCHER_PROFILES, "r") as f:
        data = json.load(f)
        # print(json.dumps(data, indent=4, sort_keys=True))
        return data

def create_profile(profile:dict):
    data = get_minecraft_profiles()
    data['profiles'][profile['name']] = profile
    data['selectedProfile'] = profile['name']
    with open(LAUNCHER_PROFILES, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)

def install_mods():
    mod_folder = os.path.join(MINECRAFT_DIR, "mods")
    if not os.path.exists(mod_folder):
        os.mkdir(mod_folder)
    for mod_file in MODS:
        print(f'Installing {mod_file} to {mod_folder}')
        shutil.copy(mod_file, mod_folder)

def install_fabric():
    m="""
_______________________________
UNCHECK THE "Create Profile" OPTION, THEN
PRESS INSTALL ON THE WINDOW THAT POPS UP!
_______________________________
Close the window that pops up when you are finished, to continue the installation.
    """
    print(m)
    subprocess.run([FABRIC_INSTALLER, '--install', '--unattended'])
    # subprocess.run(['java', '-jar', FABRIC_INSTALLER, 'client', '-dir', MINECRAFT_DIR, '-mcversion', '1.20.4', '-noprofile', '-loader', FABRIC_VERSION])

if __name__ == "__main__":
    install_fabric()
    install_mods()
    create_profile(profile)

    print("Your modpack is now installed! You can now launch it from the Minecraft Launcher.")
    input("Press enter to exit...")
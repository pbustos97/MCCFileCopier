import os
import json
from exceptions import NoFile, EmptyFile, EmptyList

#make a list of all mods
modList = []

#make a template for mods
class Mod():
    def __init__(self, fileName, target, modName):
        self.fileName = fileName
        self.target = target
        self.name = modName

#example instances for forge unlock and infinite budget
# forge = Mod('MCC-WindowsNoEditor.pak', 'MCC/Content/Paks/', 'forge')
# forgeMap = Mod('forge_halo.map', 'haloreach/maps/', 'forgeMap')

# If no file found, create empty json file of the mod list. Else add mods to the json file through overwrite
def addMods():
    global modList
    try:
        file = os.path.isfile(os.getcwd() + '\\modList.json')
        if not file:
            raise NoFile("File does not exist")
        locationFile = open('modList.json', 'w')
        global modList
        locationFile.write(json.dumps(modList, indent=4))
        locationFile.close()
    except NoFile as msg:
        createModListFile()

# If no file found, create empty json file of the mod list. Else remove mods from modList and overwrite the json file
def removeMods(mods):
    try:
        if len(mods) == 0 or mods == "\n":
            raise EmptyList("Removal list is empty")
        file = os.path.isfile(os.getcwd() + '\\modList.json')
        if not file:
            raise NoFile("File does not exist, creating modList.json")
        file = os.getcwd() + '\\modList.json'
        if os.stat(file).st_size == 0:
            raise EmptyFile("Location file is empty, cannot remove uninstalled mods")
        with open('modList.json', 'r') as json_file:
            modFile = json.load(json_file)
            for mod in mods:
                for installed in modFile:
                    if mod is installed['name']:
                        modFile.remove(installed)
            global modList
            modList = modFile
        addMods()
    except EmptyList as error:
        print(error.message)
    except NoFile as error:
        print(error.message)
        createModListFile()
    except EmptyFile as error:
        print(error.message)
    
# Creates modList file if file not found
def createModListFile():
    file = os.path.isfile(os.getcwd() + '\\modList.json')
    if not file:
        locationFile = open('modList.json', 'w')
        locationFile.close()

def mods():
    while True:
        userInput = input("Do you want to add or remove mods? [ 1 ] - Add Mods [ 2 ] - Remove Mods [ q ] - Quit: ")
        if userInput == '1':
            global modList
            counter = 0
            createModListFile()
            while True:
                userInput = input("Do you want to add a mod? [ 1 ] - Yes [ 2 ] - No: ")
                if userInput != "1":
                    break
                fileName = input("Enter the mod file name. (ex. MCC-WindowsNoEditor.pak): ")
                path = input("Enter the file path. (ex. MCC/Content/Paks/): ")
                name = input("Enter the name of the mod. (ex. Forge): ")
                modList.append(Mod(fileName, path, name).__dict__)
                counter += 1
            createModListFile()
            if counter > 0:
                addMods()
            break
        elif userInput == '2':
            print("Enter the names of the mods you want to remove. (Separate with ,): ")
            mods = input("ex. forge,forgemap,unearthed,vjlkzcj: ")
            mods = mods.split(',')
            for mod in range(0,len(mods)):
                mods[mod] = mods[mod].strip()
            removeMods(mods)
            break
        elif userInput.lower() == 'q' or userInput.lower() == 'quit':
            break

#forge = Mod('MCC-WindowsNoEditor.pak', 'MCC/Content/Paks/', 'forge')
#forgeMap = Mod('forge_halo.map', 'haloreach/maps/', 'forgeMap')
#modList.append(forge.__dict__)
#modList.append(forgeMap.__dict__)

mods()
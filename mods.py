import os

#make a list of all mods
modList = []

#make a template for mods
class Mod():
    def __init__(self, fileName, target):
        self.fileName = fileName
        self.target = target


#example instances for forge unlock and infinite budget
# forge = Mod('MCC-WindowsNoEditor.pak', 'MCC/Content/Paks/', 'forge')
# forgeMap = Mod('forge_halo.map', 'haloreach/maps/', 'forgeMap')

def addMods(modList):
    global modList
    counter = 0
    while True:
        cont = input("Do you want to add mods? [ 1 ] - Yes [ 2 ] - Remove Mods")
        if cont != "1":
            break
        print("What mods do you have installed")
        
        path = path.replace(os.sep, '/')
        newMod = Mod(fileName, path)
        modList.append(newMod)
        counter += 1

    # only triggers if user added mod
    if (counter > 0):
        #append/save new modList to file/json/xml
        print('hello world')

def removeMods():
    # open modList file
    # remove mod from file

    

def mods():
    while True:
        userInput = input("Do you want to add or remove mods? [ 1 ] - Add Mods [ 2 ] - Remove Mods")
        if userInput == '1':
            while True:
                userInput = input("Do you want to add a mod? [ 1 ] - Yes [ 2 ] - No")
                if userInput != "1":
                    break
                fileName = input("Enter the mod file name. (ex. MCC-WindowsNoEditor.pak)")
                path = input("Enter the file path. (ex. MCC/Content/Paks/)")
                addMods()
            break
        elif userInput == '2':
            print("Enter the names of the mods you want to remove. (Separate with ,)")
            mods = input("ex. forge,forgemap,unearthed,vjlkzcj")
            mods = mods.split(',')
            removeMods(mods)
            break
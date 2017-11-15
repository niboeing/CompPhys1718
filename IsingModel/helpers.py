def GetSettings():
    with open('settings.dat','r') as infile:
        settings = infile.read().splitlines()
    settingsdict = dict()
    for line in settings:
        temp = line.split('=')
        settingsdict[temp[0]] = temp[1]
    return settingsdict

def GetSize():
    settings = GetSettings()
    return int(settings['LatticeSize'])

def GetJ():
    settings = GetSettings()
    return float(settings['J'])

def GetKB():
    settings = GetSettings()
    return float(settings['kB'])

def GetTemp():
    settings = GetSettings()
    return float(settings['T'])

def GetWriteFile():
    settings = GetSettings()
    return int(settings['WriteFile'])

def GetWriteConsole():
    settings = GetSettings()
    return int(settings['WriteConsole'])

def GetFileName():
    settings = GetSettings()
    return settings['FileName']

def SetOption(key,value):
    settings = GetSettings()
    with open('settings.dat','w') as infile:
        for key2 in settings:
            if key==key2:
                write(key+'='+str(value))
            else:
                write(key+'='+settings[key])

def Output(stuff):
    if  GetWriteFile():
        with open(GetFileName(),'a') as outfile:
            outfile.write(stuff)
    if GetWriteConsole():
        print stuff

def CleanFile():
    with open(GetFileName(),'w') as outfile:
        outfile.write('')


import re
import subprocess
import time

def shutMutex():
    handle = "C:\\Users\\micha\\Repos\\RuntimeBroker\\tools\\handle64.exe"

    command = [handle, "-a \"AN-Mutex-Window-Guild Wars 2\""]
    handle_response = str(subprocess.check_output(" ".join(command)))

    pid = re.compile("pid: \d+").search(handle_response).span()
    pid = handle_response[pid[0] + 5:pid[1] + 1]

    val = re.compile("\w+: \\\\").search(handle_response).span()
    val = handle_response[val[0]:val[1] - 3]

    command = [handle, "-c %s" % val, "-p %s" % pid, "-y"]

    subprocess.call(" ".join(command))

def startSingle(self):
    # print("DEBUG 1: StartSingle: ", self.name )
    if self.name == "None":
        pass
    else:
        command = "C:\\Program Files\\Guild Wars 2\\Gw2-64.exe -autologin -nosound -shareArchive"
        # command = "D:\\Program Files\\Guild Wars 2\\Gw2-64.exe -autologin -nosound -shareArchive"

        if self.datFile:
            Account.linkDat(self)

        subprocess.Popen(command)

        time.sleep(10)
        Account.shutMutex()

        self.lastLogin = datetime.today().strftime('%H:%M:%S')
        window.updateLastLogin(self)
        window.prepareNames(self)
        window.updateButton(self)
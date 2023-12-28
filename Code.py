import subprocess
import time
import ctypes, sys
import time
import os
import uuid
import getpass

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_emulators():
    command = "E:\\LDPlayer\\LDPlayer9\\ldconsole.exe list2"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8')
    error = error.decode('utf-8')

    if process.returncode == 0:
        #print("Output:\n", output)
        return output
    else:
import subprocess
import time
import ctypes, sys
import time
import os
import uuid
import getpass

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_emulators():
    command = "E:\\LDPlayer\\LDPlayer9\\ldconsole.exe list2"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8')
    error = error.decode('utf-8')

    if process.returncode == 0:
        #print("Output:\n", output)
        return output
    else:
        print("Error:\n", error)

def convert(data):
    get_lines = data.strip().split('\n')
    headers = ["Index", "Title", "Top Window Handle", "Bind Window Handle", "Android Started", "PID", "PID of Vbox", "Resolution Width", "Resolution Height", "Unknown"]
    __list = []

    for i in get_lines:
        v = i.split(',')
        v2 = dict(zip(headers, v))
        __list.append(v2)

    return __list


def install_autorejoin(id): 
    ld = "E:\\LDPlayer\\LDPlayer9\\ldconsole.exe" + (" installapp --index {0} --filename " +os.path.abspath(__file__) + "Aqua.apk").format(id)
    subprocess.run(ld,shell=True)
def tranduythieunang(id):
    ld = "E:\\LDPlayer\\LDPlayer9\\ldconsole.exe" + (" runapp --index {0} --packagename com.aqua.hub").format(id)
    subprocess.run(ld,shell=True)

def wait_emulator(id):
    Started = False
    while Started == False:
        mydata =convert(get_emulators())
        if mydata[int(id)]["Android Started"] == "1":
            Started = True
        time.sleep(1)

    print("Emulator " + id + " Started, Running Auto Join Roblox")
    time.sleep(1)

def generate_key():
    return uuid.uuid4().hex

def store_key(key):
    with open("key.txt", "w") as f:
        f.write(key)

def retrieve_key():
    with open("key.txt", "r") as f:
        return f.read().strip()

def validate_key(key):
    return key == retrieve_key()

if __name__ == "__main__":

    éœ€è¦æ‰“å¼€ = [1,2,3,4,5,6] #[List Of Emulator you want to open][Index Starts From 0]

    if is_admin():
        data_list =convert(get_emulators())
        for data in data_list:
            print(data)
            if int(data['Index']) in éœ€è¦æ‰“å¼€ and data["Android Started"] == "0":
                openLD(data['Index'])
                wait_emulator(data['Index']) # [Wait Till Emulator Starts]

                # **Key Generation**
                key = generate_key()

                # **Key Input**
                print("Enter key: ")
                input_key = getpass.getpass()

                # **Key Validation**
                if validate_key(input_key):
                    print("Key is valid.")

                    tranduythieunang(data['Index'])
                else:
                    print("Key is invalid.")

                time.sleep(1)

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
￼Enter        print("Error:\n", error)

def convert(data):
    get_lines = data.strip().split('\n')
    headers = ["Index", "Title", "Top Window Handle", "Bind Window Handle", "Android Started", "PID", "PID of Vbox", "Resolution Width", "Resolution Height", "Unknown"]
    __list = []

    for i in get_lines:
        v = i.split(',')
        v2 = dict(zip(headers, v))
        __list.append(v2)

    return __list


def install_autorejoin(id): 
    ld = "E:\\LDPlayer\\LDPlayer9\\ldconsole.exe" + (" installapp --index {0} --filename " +os.path.abspath(__file__) + "Aqua.apk").format(id)
    subprocess.run(ld,shell=True)
def tranduythieunang(id):
    ld = "E:\\LDPlayer\\LDPlayer9\\ldconsole.exe" + (" runapp --index {0} --packagename com.aqua.hub").format(id)
    subprocess.run(ld,shell=True)

def wait_emulator(id):
    Started = False
    while Started == False:
        mydata =convert(get_emulators())
  if mydata[int(id)]["Android Started"] == "1":
            Started = True
        time.sleep(1)

    print("Emulator " + id + " Started, Running Auto Join Roblox")
    time.sleep(1)

def generate_key():
    return uuid.uuid4().hex

def store_key(key):
    with open("key.txt", "w") as f:
        f.write(key)

def retrieve_key():
    with open("key.txt", "r") as f:
        return f.read().strip()

def validate_key(key):
    return key == retrieve_key()

if __name__ == "__main__":

    éœ€è¦æ‰“å¼€ = [1,2,3,4,5,6] #[List Of Emulator you want to open][Index Starts From 0]

    if is_admin():

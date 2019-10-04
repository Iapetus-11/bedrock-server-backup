import subprocess
import threading
from time import sleep
from os import system

#open new process opening bedrock_server.exe
process = subprocess.Popen('bedrock_server.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#allows for input from the console
def InputLoop():
    while True:
        inp = input() + "\n"
        process.stdin.write(inp.encode())
        process.stdin.flush()

#output from bedrock_server.exe
def OutputLoop():
    while True:
        for line in process.stdout:
            line = str(line).replace("b'","")[:-5]
            print(line)

#backing up loop
def BackupLoop():
    while True:
        toType = "save hold" + "\n"
        process.stdin.write(toType.encode())
        process.stdin.flush()
        sleep(7.5)
        system("backup.bat")
        sleep(.75)
        toType = "save resume" + "\n"
        process.stdin.write(toType.encode())
        process.stdin.flush()
        sleep(3600)

#start the threads
outputt = threading.Thread(target=InputLoop)
inputt = threading.Thread(target=OutputLoop)

outputt.start()
inputt.start()

sleep(15)
BackupLoop()

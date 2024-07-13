import re
import pyfiglet

'''def file():
    text = input("[+] Enter Name of Log File: ") #text = "log.txt"
    return text'''
def intro():
    #from colorama import Fore
    styled_text = pyfiglet.figlet_format('I N F O C U R E', font='slant')
    print(styled_text, "\t> by Abhay Rastogi | Securing Your Data, Securing Your Future...")
def auth_failure(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m'''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\(\w+\)\[\d+\]:\s+authentication\s+failure.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\(\w+\).+\[\d+\]:\s+authentication\s+failure.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.\d+.:\s+Kerberos\s+authentication\s+failed|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.\d+.:\s+Authentication\s+failed\s+from.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\sCouldn't\sauthenticate.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\sCouldn't\sauthenticate.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[*] AUTHENTICATION FAILURE LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def session_alerts(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\(\w+\)\[\d+\]:\s+session\s+opened.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\(\w+\).+\[\d+\]:\s+session\s+opened.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\(\w+\)\[\d+\]:\s+session\s+closed.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+:\s+ALERT.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[*] SESSION OPENED/CLOSED/LOGROTATE ALERT :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def connection(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+connection\s+from.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+connection\s+from.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+\w+\s+\w+\s+timed\s+out.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+\w+\s+\w+\s+timed\s+out.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print(
            "[*] CONNECTION FROM USERS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def start_stop_restart(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.\s+\w+\s+shutdown\s+.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.\s+\w+\s+startup\s+.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.\s+\w+.+\s+startup\s+.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+syslogd.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+\w+\s+\d+.\d+.\d+\s+Starting|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+\w+\s+\d+.\d+.\d+\s+Starting.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+\w+.+\s+.+started"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print(
            "[*] START/SHUTDOWN/RESTART :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def auto_detect(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+\*+\s+info\s+\[.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+\*+\s+info\s+\[.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+\w+:\s+Auto-detected.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+\w+:\s+Auto-detected.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[*] AUTO-DETECTION LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def login(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\-+\s+\w+.+\[\d+\]:\s+\w+\s+LOGIN\s+ON.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\-+\s+\w+\[\d+\]:\s+\w+\s+LOGIN\s+ON.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[*] LOGIN USERS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()

def operations(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+removing\s+device.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+removing\s+device.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+creating\s+device.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+creating\s+device.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[*] CREATING/REMOVING DEVICE NODES :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def warnings(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\snotify\squestion.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\snotify\squestion.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+\w+\s+\(\w+\):\s+\w+\s+endpoint.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+\w+\s+\(\w+\):\s+\w+\s+endpoint.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+.+\[\d+\]:\s+warning:.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\w+\[\d+\]:\s+warning:.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[*] NOTIFY QUESTION/ENDPOINTS/WARNINGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def system_logs(text):

    '''class Format:
        end = '\033[0m'
        underline = '\033[4m' '''

    with open(text, "r") as file:
        pattern = "\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+kernel:.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+random:.+|\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+network:.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[*] KERNEL/RANDOM/NETWORK LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def load(text1):
    '''class Format:
        end = '\033[0m'
        underline = '\033[4m'''

    with open(text1, "r") as file:
        pattern = "\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Loaded.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[+] LOADED SERVICE LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def init(text1):
    '''class Format:
        end = '\033[0m'
        underline = '\033[4m'''

    with open(text1, "r") as file:
        pattern = "\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+0+\d+.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Scavenge:.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Ending.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Starting.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+\w+\s+service\s+starts\s+successfully.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+No\s+startup\s+processing\s+required.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+NonStart:.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Startup.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[+] INITIALIZE LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def sqm(text1):
    '''class Format:
        end = '\033[0m'
        underline = '\033[4m'''

    with open(text1, "r") as file:
        pattern = "\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+SQM:.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[+] SOFTWARE QUALITY METRICS(SQM) LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def session(text1):
    '''class Format:
        end = '\033[0m'
        underline = '\033[4m'''

    with open(text1, "r") as file:
        pattern = "\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Session:.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Failed\s+to\s+internally\s+open\s+package.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Read\s+out\s+cached\s+package\s+applicability\s+for\s+package:.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[+] SESSION LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def warning_window(text1):
    '''class Format:
        end = '\033[0m'
        underline = '\033[4m'''

    with open(text1, "r") as file:
        pattern = "\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Warning:.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Expecting\s+attribute\s+name.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Failed\s+to\s+get\s+next\s+element.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[+] WARNING/EXPECTING/FAILED LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def loading(text1):
    '''class Format:
        end = '\033[0m'
        underline = '\033[4m'''

    with open(text1, "r") as file:
        pattern = "\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Loading\s+offline\s+registry\s+hive:.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Unloading\s+offline\s+registry\s+hive:.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Offline\s+image\s+is:.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Disabling\s+manifest\s+caching,.+|\d+-\d+-\d+\s+\d+:\d+:\d+,\s+\w+\s+\w+\s+Enable\s+manifest\s+caching,.+"
        file = file.read()
        refine = re.findall(pattern, file)
        count = len(refine)
        size = len(refine[0])
        size = size + 10
        i = 0
        print("[+] LOADING/UNLOADING OFFLINE REGISTRY LOGS :-")
        print("\t\t* Number of logs:", count)
        print("-" * size)
        while i < count:
            print(refine[i])
            i = i + 1
    print()
def linux(text):
    print("[*] LINUX OPTIONS :-")
    print("\t\t[1.] AUTHENTICATION FAILURE LOG.")
    print("\t\t[2.] SESSION OPENED/CLOSED/LOGROTATE ALERT LOG.")
    print("\t\t[3.] CONNECTION FROM USERS LOG.")
    print("\t\t[4.] START/SHUTDOWN/RESTART LOG.")
    print("\t\t[5.] AUTO-DETECTION LOG.")
    print("\t\t[6.] LOGIN USERS LOG.")
    print("\t\t[7.] CREATING/REMOVING DEVICE NODES LOG.")
    print("\t\t[8.] NOTIFY QUESTION/ENDPOINTS/WARNINGS LOG.")
    print("\t\t[9.] KERNEL/RANDOM/NETWORK LOG.")
    print("\t\t[10.] ALL OF THE ABOVE.")
    print("\t\t[11.] BACK TO PREVIOUS MENU.")
    print("\t\t[12.] EXIT.")
    print()
    linux_option = input("[+] Enter your choice: ")
    print()
    if linux_option == "1":
        auth_failure(text)
        linux(text)
        print()
    elif linux_option == "2":
        session_alerts(text)
        linux(text)
        print()
    elif linux_option == "3":
        connection(text)
        linux(text)
        print()
    elif linux_option == "4":
        start_stop_restart(text)
        linux(text)
        print()
    elif linux_option == "5":
        auto_detect(text)
        linux(text)
        print()
    elif linux_option == "6":
        login(text)
        linux(text)
        print()
    elif linux_option == "7":
        operations(text)
        linux(text)
        print()
    elif linux_option == "8":
        warnings(text)
        linux(text)
        print()
    elif linux_option == "9":
        system_logs(text)
        linux(text)
        print()
    elif linux_option=="10":
        auth_failure(text)
        session_alerts(text)
        connection(text)
        start_stop_restart(text)
        auto_detect(text)
        login(text)
        operations(text)
        warnings(text)
        system_logs(text)
        linux(text)
        print()
    elif linux_option=="11":
        option()
        print()
    elif linux_option=="12":
        print()
        print("Thank you for choosing INFOCURE. Your trust is our priority!")
        print()

def windows(text1):
    print("[*] WINDOWS OPTIONS :-")
    print("\t\t[1.] LOADED SERVICE LOG.")
    print("\t\t[2.] INITIALIZE LOG.")
    print("\t\t[3.] SOFTWARE QUALITY METRICS(SQM) LOG.")
    print("\t\t[4.] SESSION LOG.")
    print("\t\t[5.] WARNING/EXPECTING/FAILED LOG.")
    print("\t\t[6.] LOADING/UNLOADING OFFLINE REGISTRY LOG.")
    print("\t\t[7.] ALL OF THE ABOVE.")
    print("\t\t[8.] BACK TO PREVIOUS MENU.")
    print("\t\t[9.] EXIT.")
    print()
    window_option = input("[+] Enter your choice: ")
    print()
    if window_option == "1":
        load(text1)
        windows(text1)
        print()
    elif window_option == "2":
        init(text1)
        windows(text1)
        print()
    elif window_option== "3":
        sqm(text1)
        windows(text1)
        print()
    elif window_option == "4":
        session(text1)
        windows(text1)
        print()
    elif window_option == "5":
        warning_window(text1)
        windows(text1)
        print()
    elif window_option == "6":
        loading(text1)
        windows(text1)
        print()
    elif window_option == "7":
        load(text1)
        init(text1)
        sqm(text1)
        session(text1)
        warning_window(text1)
        loading(text1)
        windows(text1)
        print()
    elif window_option == "8":
        option()
        print()
    elif window_option == "9":
        print()
        print("Thank you for choosing INFOCURE. Your trust is our priority!")
        print()
def option():
    print("[*] OPTIONS :-")
    print("\t\t[1.] Linux Log.")
    print("\t\t[2.] Windows Log.")
    print()
    option = input("[+] Choose your Option: ")
    print()
    match option:
        case "1":
            text = input("[+] Enter Name of Log File: ")  # text = "log.txt"
            linux(text)

        case "2":
            text1 = input("[+] Enter Name of Log File: ")  # text = "log.txt"
            windows(text1)

intro()
print()
option()
print()
#text=file()


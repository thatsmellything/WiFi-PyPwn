import os, platform

#https://lawsie.github.io/guizero/

#Scripts for installation


if platform.system() == "linux":
    os.system("sudo apt install python3 python3-tk aircrack-ng -yy")
    os.system("sudo pip3 install -r requirements.txt")
elif platform.system() == "win32":
    print("windows is a unsupported platform")
elif platform.system() == "Darwin":
    os.system("sudo pip3 install -r requirements.txt")
        
else:
    print("Unsupported platform")
    print(platform.system())
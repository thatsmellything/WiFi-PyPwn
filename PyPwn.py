from guizero import App, Window, PushButton, Text, TextBox, Picture, Box, Slider, CheckBox, ListBox, Combo
import os
import platform, time







#TEST ME
def scan_wifiAccessPoints_to_file():
    if platform.system() == "Linux":
        os.system("sudo airmon-ng start " + input_box.value)
        os.system("sudo airodump-ng " + input_box.value + "mon > scanAPs.txt")
        time.sleep(5)
        os.system("sudo airmon-ng stop " + input_box.value + "mon")
    elif platform.system() == "win32":
        print("windows is a unsupported platform")
    elif platform.system() == "Darwin":
        os.system("sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s > scanAPs.txt")
        
    else:
        print("Unsupported platform")
        print(platform.system())
#os.system("sudo airmon-ng -h > test.txt")




#GUI Backend
def open_APScanner_window():
    scan_wifiAccessPoints_to_file()
    
    APScanner_window.show()
    

def close_APScanner_window():
    APScanner_window.hide()

def open_Scan4Devices_window():
    Scan4Devices_window.show()

def close_Scan4Devices_window():
    Scan4Devices_window.hide()



#GUI Portion
PyPwn = App(title="PyPwn")

#Window sections
APScanner_window = Window(PyPwn, title="Scan4AccessPoints")
APScanner_window.hide()

Scan4Devices_window = Window(PyPwn, title="Scan4Devices")
Scan4Devices_window.hide()

#Buttons and inputs
input_box = TextBox(PyPwn, text="Input name of scanning device")
text = Text(APScanner_window, text=open("scanAPs.txt", "r").read())

open_button = PushButton(PyPwn, text="Open AP Scanner", command=open_APScanner_window)
close_button = PushButton(APScanner_window, text="Close", command=close_APScanner_window)

Scan4Devices_button = PushButton(PyPwn, text="Open Device Scanner", command=open_Scan4Devices_window)
Scan4Devices_button = PushButton(Scan4Devices_window, text="Close", command=close_Scan4Devices_window)

PyPwn.display()
from guizero import App, Window, PushButton

def open_APScanner_window():
    APScanner_window.show()

def close_APScanner_window():
    APScanner_window.hide()

def open_Scan4Devices_window():
    Scan4Devices_window.show()

def close_Scan4Devices_window():
    Scan4Devices_window.hide()

app = App(title="PyPwn")

APScanner_window = Window(app, title="Scan4AccessPoints")
APScanner_window.hide()

Scan4Devices_window = Window(app, title="Scan4Devices")
Scan4Devices_window.hide()

open_button = PushButton(app, text="Open AP Scanner", command=open_APScanner_window)
close_button = PushButton(APScanner_window, text="Close", command=close_APScanner_window)

Scan4Devices_button = PushButton(app, text="Open Device Scanner", command=open_Scan4Devices_window)
Scan4Devices_button = PushButton(Scan4Devices_window, text="Close", command=close_Scan4Devices_window)

app.display()
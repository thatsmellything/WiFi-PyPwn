from guizero import App, Window, PushButton

import gui_backend

app = App(title="PyPwn")

APScanner_window = Window(app, title="Scan4AccessPoints")
APScanner_window.hide()

Scan4Devices_window = Window(app, title="Scan4Devices")
Scan4Devices_window.hide()

open_button = PushButton(app, text="Open AP Scanner", command=gui_backend.open_APScanner_window)
close_button = PushButton(APScanner_window, text="Close", command=gui_backend.close_APScanner_window)

Scan4Devices_button = PushButton(app, text="Open Device Scanner", command=gui_backend.open_Scan4Devices_window)
Scan4Devices_button = PushButton(Scan4Devices_window, text="Close", command=gui_backend.close_Scan4Devices_window)

app.display()
#!/usr/bin/python3 -B
"""
Main entry to the pygame program
"""

import window
import window_control

WIN = window.MainWindow(1280, 720)
CONT = window_control.Controller()
WIN.register(CONT, CONT.notify)
WIN.mainloop()
print("Done")

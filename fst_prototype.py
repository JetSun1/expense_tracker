#fst_prototype.py

import PySimpleGUI as sg

layout = [[sg.Text("Hello from Paris !!")], [sg.Button("OK")]]


#create the window 
window = sg.Window("Premiers test concluants !", layout)

#create an event loop
while True:
    event, values = window.read()

    #End program if user closes window or
    #presses the OK button 
    if event == "OK" or even == sg.WIN_CLOSED:
        break

window.close()
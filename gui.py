import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")


# layout merupakan list, didalam layout terdapat list yg represent row("[]"), satu list berarti satu row
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()


import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

output_label = sg.Text("", key="output")
button = edit_button = sg.Button("Convert")
window = sg.Window("Convertor",
                   layout=[[label1, input1], [label2, input2], [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = feet * 0.3048 + inches * 0.0254

    window["output"].update(value=f"{result} m", text_color="white")

window.close()

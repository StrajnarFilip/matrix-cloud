import PySimpleGUI as sg


def run_gui():
    layout = [[sg.Text('Username', size=(8, 1)),
               sg.Input(key="username")],
              [
                  sg.Text('Password', size=(8, 1)),
                  sg.Input(password_char="*", key="password")
              ],
              [
                  sg.Text('Upload file', size=(8, 1)),
                  sg.Input(key="file_name"),
                  sg.FileBrowse()
              ],
              [
                  sg.Radio('Download', 1, default=True, key="download_choice"),
                  sg.Radio('Upload', 1, key="upload_choice")
              ], [sg.Button('Start')]]

    window = sg.Window('Matrix Cloud GUI', layout)
    input_values = window.read()
    if input_values == None:
        return
    _, values = input_values
    print(values)

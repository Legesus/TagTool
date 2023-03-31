# Built using vscode-ext

import sys
import vscode

ext = vscode.Extension(name = "TestTool", display_name = "Test Tool", version = "0.0.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"

@ext.command()
def hello_world():
    vscode.window.show_info_message(f'Hello World from {ext.name}')



def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()

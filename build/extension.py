# Built using vscode-ext

import sys
import vscode

ext = vscode.Extension(name="TestTool", display_name="Test Tool", version="0.1.0")

@ext.event
async def on_activate():
    vscode.log(f"The Extension '{ext.name}' has started")


@ext.command()
async def hello_world(ctx):
    return vscode.window.show.info.message(f"Hello World from {ext.name}")



def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
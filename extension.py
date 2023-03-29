import vscode

ext = vscode.Extension(name="TestTool", display_name="Test Tool", version="0.1.0")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"


@ext.command()
def hello_world():
    return vscode.window.show.info.message(f"Hello World from {ext.name}")

vscode.build(ext)
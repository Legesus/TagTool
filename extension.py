import vscode

ext = vscode.Extension(name="TestTool")

@ext.event
async def on_activate():
    vscode.log(f"The Extension '{ext.name}' has started")


@ext.command()
async def hello_world(ctx):
    return await ctx.show(InfoMessage(f"Hello World from {ext.name}"))

ext.run()
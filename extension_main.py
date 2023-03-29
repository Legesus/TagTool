import json
import vscode

def activate(context):
    snippets = {
        "Hello World": {
            "prefix": "hw",
            "body": [
                "print('Hello World')"
            ],
            "description": "Prints 'Hello World'"
        }
    }
    context.subscriptions.append(
        vscode.languages.registerCompletionItemProvider(
            "python",
            {
                "provideCompletionItems": lambda document, position, token, context: [
                    vscode.CompletionItem(key, vscode.CompletionItemKind.Snippet)
                    .with_insert_text(value["body"][0])
                    .with_documentation(value["description"])
                    for key, value in snippets.items()
                ]
            }
        )
    )

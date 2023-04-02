# Built using vscode-ext

import sys
import os
import vscode
import pdf_to_xml

from pdf_to_xml import parse_pdf_to_xml
from importlib.resources import path


ext = vscode.Extension(name = "TestTool", display_name = "Test Tool", version = "0.0.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"

@ext.command()
def hello_world():
    vscode.window.show_info_message(f'Hello World from {ext.name}')

@ext.command(title="Pdf2XML")
def parse_pdfs_to_xml(directory):

    vscode.window.show_info_message(f'Starting Pdf2XML....')
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Get the full path of the file
        filepath = os.path.join(directory, filename)
        # Check if the file is a PDF file
        if os.path.isfile(filepath) and filename.lower().endswith('.pdf'):
            # Call the parse_pdf_to_xml function on the PDF file
            xml_tree = parse_pdf_to_xml(filepath)
            # Generate the XML file name based on the PDF file name
            xml_path = filepath.replace('.pdf', '.xml')
            # Write the XML data to a file
            xml_tree.write(xml_path)

    pdf_directory = 'D:/Projects/Work/ExtensionProgramming/PDF'
    parse_pdfs_to_xml(pdf_directory)
    vscode.window.show_info_message(f'Ending Pdf2XML....')


def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()

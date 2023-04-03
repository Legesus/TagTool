import PyPDF2
import xml.etree.ElementTree as ET

def parse_pdf_to_xml(pdf_path):
    # Create a PDF reader object
    print("Hello this is pdf2xml.py")
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Create an ElementTree object to hold the XML data
        xml_tree = ET.ElementTree()
        # Create a root element for the XML data
        root = ET.Element('pdf')
        # Loop through each page in the PDF file
        for page_num in range(pdf_reader.getNumPages()):
            # Get the page object for the current page
            page = pdf_reader.getPage(page_num)
            # Create a page element for the XML data
            page_elem = ET.SubElement(root, 'page', {'number': str(page_num)})
            # Loop through each text object on the page
            for text_obj in page.extractText().split('\n'):
                # Create a text element for the XML data
                text_elem = ET.SubElement(page_elem, 'text')
                # Set the text content of the element
                text_elem.text = text_obj
        # Set the root element of the XML tree
        xml_tree = ET.ElementTree(root)
        # Generate the XML file name based on the PDF file name
        xml_path = pdf_path.replace('.pdf', '.xml')
        # Write the XML data to a file
        xml_tree.write(xml_path)
        # Return the XML tree
        return xml_tree


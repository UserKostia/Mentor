from json import dumps
from xmltodict import parse
from classes.nmap_scanner import NmapScanner


# Default IP to scan
ip = "94.243.121.4"

# Path to the Nmap executable
nmap_path = 'C:\\Program Files (x86)\\Nmap\\nmap.exe'

# Some options to scan IP address
options = ["-sS", "-sU", "-sV", "-vv", "-F", "-oX", "nmap_result\\results.xml"]


# Creates object and scans it
nmap_test = NmapScanner(ip, nmap_path, options)
result = nmap_test.scan()
print(f"{result = }")


# Open the resulting XML file and read its content
with open("nmap_result\\results.xml", "r") as f:
    xml_file = f.read()


# Converts the XML file content to a dictionary
xml_dict = parse(xml_file)


# Shows results in a JSON-like format with indentation
print("\nXML TO DICT:")
print(dumps(xml_dict, indent=4))

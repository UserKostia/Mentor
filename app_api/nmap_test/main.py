from json import dumps
from xmltodict import parse
from classes.nmap_scanner import *


ip = "94.243.121.4"
nmap_path = 'C:\\Program Files (x86)\\Nmap\\nmap.exe'
options = ["-sS", "-sU", "-sV", "-vv", "-F", "-oX", "nmap_result\\results.xml"]


nmap_test = NmapScanner(ip, nmap_path, options)
result = nmap_test.scan()
print(f"{result = }")


with open("nmap_result\\results.xml", "r") as f:
    xml_file = f.read()

xml_dict = parse(xml_file)

print("\nXML TO DICT:")
print(dumps(xml_dict, indent=4))

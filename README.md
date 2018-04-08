# Arduino-web-app-helper

WiFi enabled Arduinos can send static sites to local machines byte by byte. There are two time-consuming challenges here:
1. an escape character must be inserted before each inverted comma of inline stylings.
2. each line must be wrapped in a call to clinet.println()

This python script reads an html file and output a text file to meet the above requirements. 
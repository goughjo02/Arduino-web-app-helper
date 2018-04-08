# Arduino-web-app-helper

WiFi enabled Arduinos can send static sites to local machines byte by byte. There are two time-consuming challenges here:
1. an escape character must be inserted before each inverted comma of inline stylings.
2. each line must be wrapped in a call to client.println()

This python script reads an html file and output a text file to meet the above requirements. 

Hack without impediment.
# To use:
1. git clone this repo.
2. Replace file 'input.html' with your own html file. Name it 'input.html'
3. From command line run `python convert.py`
4. Open file 'Output.txt' and enjoy the fruits of efficient coding.
"""
Script to help present local web apps via arduino.

Read html and output version suitable for arduino 'client.println' function.
"""

import codecs

f = codecs.open("input.html", 'r')
full_page = f.read()
c = '"'
inverted_commas = ([pos for pos, char in enumerate(full_page) if char == c])
for i in inverted_commas:
    full_page = full_page[:(i + inverted_commas.index(i))] + "\\" \
        + full_page[(i + inverted_commas.index(i)):]
text_file = open("Output.txt", "w")
text_file.write(full_page)
text_file.close()
converted_string = ""
with open("Output.txt") as f:
    for line in f:
        newline = ("client.println(\"%s\");\n" % line[:-1])
        converted_string = converted_string + newline
text_file = open("Output.txt", "w")
text_file.write(converted_string)
text_file.close()

#!/usr/bin/python3.13
import sys as s
import os

# Variables
dir_prog = "/home/salah/Documents/.programming/Bash/Developer/Project/Command/dirprogramming"
lang = s.argv[1]
short_lang = s.argv[2]
style = s.argv[3]

# Read 'dirprogramming' file
data = []
with open(dir_prog, 'r') as file:
    for word in file.readlines():
        data.append(word[0:-1])
    file.close()

# The information of this language to be added in the 'dirprogramming' file
info = f'''elif [ "$lang" = "{short_lang}" ]; then
   cd {lang}
   navigate
fi'''

# Insert the information of this language to the new data list
new_data = data[0:-1]
for item in info.split("\n"):
    new_data.append(item)

# Now writing that new data list to the 'dirprogramming' file
#with open(dir_prog, 'w') as file:
#    for word in "\n".join(new_data):
#        file.write(word)
#    file.close()

# Directory structure
dir_structure = {
    '1': {
        f"{lang}": [f"{lang}/Developer", f"{lang}/Project", f"{lang}/Virtual\\ Environment", f"{lang}/Web"],
        "Developer": [f"{lang}/Developer/Project", f"{lang}/Developer/Quick", f"{lang}/Developer/Tutorial"],
        "Developer/Tutorial": [f"{lang}/Developer/Tutorial/Basic", f"{lang}/Developer/Tutorial/Learn"]
    },
    '2': {
        f"{lang}": [f"{lang}/Developer", f"{lang}/Project", f"{lang}/Virtual\\ Environment", f"{lang}/Web"],
        "Developer": [f"{lang}/Developer/Project", f"{lang}/Developer/Quick", f"{lang}/Developer/Tutorial", f"{lang}/Developer/Package"],
        "Developer/Project": [f"{lang}/Developer/Project/Command"],
        "Developer/Tutorial": [f"{lang}/Developer/Tutorial/Basic", f"{lang}/Developer/Tutorial/Learn"]
    }
}

# Create directories and subdirectories for this language
if style == '1':
    for parent in dir_structure["1"].keys():
        for child in dir_structure["1"][parent]:
            os.system(f"mkdir -p {child}")
elif style == '2':
    for parent in dir_structure["2"].keys():
        for child in dir_structure["2"][parent]:
            os.system(f"mkdir -p {child}")

# script which was used to dump jsons from dictonary

import json

def clean_string(s):
    return s.encode('utf-8', 'ignore').decode('utf-8')
    # return s.replace("\u200c","").replace("\u00A0","").replace('\u200e',"").replace("\u200f","")


lan = ["as","bn","gom","gu","hi","kn","ks","mai","ml","mr","or","pa","sa","sat","sd","ta","tcy","te","ur"]

for each in lan:

    with open(f"{each}_wordlist.combined","r",encoding="utf-8") as f:
        f.readline()
        data = f.readlines()

    final = {}
    for ele in data:
        temp = ele[:-1].split(",")
        final[clean_string(temp[0]).split("=")[1]] = int(temp[1].split("=")[1])


    with open(f'jsons/{each}.json', 'w', encoding ='utf-8') as json_file:
        json.dump(final, json_file, indent = 2, ensure_ascii = False)
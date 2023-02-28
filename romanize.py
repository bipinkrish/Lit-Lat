from indictrans import Transliterator
import json

lit = Transliterator(source='kan', target='eng', build_lookup=True)

with open("dictionary/kn.json", "r", encoding="utf-8") as f:
    wordss = json.load(f)

romanized = {}
for key, value in wordss.items():
    romanized[lit.transform(key)] = value

with open('romanized/kn.json', 'w') as json_file:
    json.dump(romanized, json_file, indent = 2)

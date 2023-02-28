# script used to romanize

from indictrans import Transliterator
import json
from shared import langs
import os

for name, lang in langs.items():

    if lang[1] is None or os.path.exists(f'romanized/{lang[0]}.json'): continue

    lit = Transliterator(source=lang[0], target='eng', build_lookup=True)

    with open(f"dictionary/{lang[1]}.json", "r", encoding="utf-8") as f:
        words = json.load(f)

    romanized = {}
    for key, value in words.items():
        eng = lit.transform(key)
        if eng not in romanized:
            romanized[eng] = value


    with open(f'romanized/{lang[0]}.json', 'w') as json_file:
        json.dump(romanized, json_file, indent = 2)

    print(name, "completed")
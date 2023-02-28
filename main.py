# setup
from worker import get_closest_match_for_sentence
from shared import langs
comm_lang = langs["Kannada"]
src_text = "baa manege amele mari beda"

# lit
from indictrans import Transliterator
lit = Transliterator(source='eng', target=comm_lang[0], build_lookup=True)

# lat
from googletrans import Translator
lat = Translator()

# print 1
print("\nFor using Dict at 1st step\n")
print("source text is", src_text)

# checking in dictonary of source
dict_src_text = get_closest_match_for_sentence(src_text, f"romanized/{comm_lang[0]}.json")
print("closest match found for", src_text, "is", dict_src_text)

# litting 1
local_lang_dict = lit.transform(dict_src_text)
print("Lited", dict_src_text, "to", local_lang_dict)

# latting 1
eng_lang_1 = lat.translate(local_lang_dict).text
print("Lated", local_lang_dict, "to", eng_lang_1)

print("\n")

# print 2
print("\nFor using Dict at 2nd step\n")
print("source text is", src_text)

# litting 2
local_lang_src = lit.transform(src_text)
print("Lited", src_text, "to", local_lang_src)

# checking in dictonary of litted
dict_local_text = get_closest_match_for_sentence(local_lang_src, f"dictionary/{comm_lang[1]}.json")
print("closest match found for", local_lang_src, "is", dict_local_text)

# latting 2
eng_lang_2 = lat.translate(dict_local_text).text
print("Lated", dict_local_text, "to", eng_lang_2)

print("\n")

# print 3
print("\nWithout using Dict\n")
print("source text is", src_text)

# Litting 3
print("Lited", src_text, "to", local_lang_src)

# Latting 4
no_dict_eng = lat.translate(local_lang_src).text
print("Lated", local_lang_src, "to", no_dict_eng)

print("\n")

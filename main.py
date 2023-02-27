# lit

from indictrans import Transliterator
lit = Transliterator(source='eng', target='kan', build_lookup=True)

text = "baa manege"
kan = lit.transform(text)
print(kan)


# lat

from translate import Translator # from googletrans import Translator
lat = Translator(from_lang="kn",to_lang="en") # lat = Translator()

eng = lat.translate(kan) # ,src='kn', dest='en')
print(eng)

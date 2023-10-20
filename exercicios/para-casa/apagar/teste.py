#teste


from googletrans import Translator
# create a translator object
translator = Translator()

# use translate method to translate a string - by default, the destination language is english
translated = translator.translate('Hola Mundo')

# the translate method returns an object
print(translated)
# Translated(src=es, dest=en, text=Hello World, pronunciation=Hello World, extra_data="{'translat...")

# obtain translated string by using attribute .text
translated.text
# 'Hello World'



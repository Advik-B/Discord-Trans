import googletrans

_available_lang = googletrans.LANGUAGES.items()

langs = dict()
langs2 = dict()

ON = True
OFF = False

class TranslateError(Exception):
    pass
class AutoDectectError(Exception):
    pass

for lang_prefix , lang in _available_lang:
    langs.update({str(lang_prefix): str(lang)})
    langs2.update({str(lang) : str(lang_prefix)})

trans = googletrans.Translator()

def _convert(
    text:str,

    output_lang:str='en',

    auto_dectect:bool=ON,

    source:str=None,

    ):
    """Will translate the text in given language
    -"""
    if source == None:
        _source = 'en'
    else:
        if source in langs2.keys():
            __out = langs2[source]
        elif source in langs.keys():
            __out = langs[source]
        else:
            raise TranslateError(f'No language match with `{output_lang}`')
        _source = source

    if auto_dectect == OFF:

        if output_lang in langs2.keys():
            __out = langs2[output_lang]
        elif output_lang in langs.keys():
            __out = langs[output_lang]
        else:
            raise TranslateError(f'No language match with `{output_lang}`')

        _out = trans.translate(text , src = _source , dest=output_lang)
        return _out.text

    elif auto_dectect == ON:
        if output_lang in langs2.keys():
            __out = langs2[output_lang]
        elif output_lang in langs.keys():
            __out = langs[output_lang]
        else:
            raise TranslateError(f'No language match with `{output_lang}`')

        _out = trans.translate(text , dest=output_lang)
        return _out.text
    
    else:
        raise AutoDectectError(f'Unknown Auto-Dectect mode :{auto_dectect}')


def convert(
    text:str,

    output_lang:str='en',

    auto_dectect:bool=ON,

    source:str=None,
    ):


    _raw_out = _convert(text , output_lang , auto_dectect , source)
    return _raw_out

print(convert('Bonjour'))
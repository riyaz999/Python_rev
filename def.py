def greet(lang):
    if lang == 'es':
        return 'english'
    elif lang == 'sh':
        return "bash"
    else:
        return 'blast'


print(greet('es'))
print(greet('sh'))

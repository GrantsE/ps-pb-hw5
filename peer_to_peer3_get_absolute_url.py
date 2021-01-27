def get_absolute_url(url, *args, **kwargs):
    #создаем переменную, куда будут передаваться параметры *args в виде списка
    positional_arguments = []  
    #проходимся циклом for по параметрам *args и добавляем в переменную positional_arguments
    for i in args:
        positional_arguments.append(i)
    #изменяем тип переменной positional_arguments на str и удаляем/заменяем некоторые символы
    positional_arguments = str(positional_arguments).replace(",", "/").replace(" ", "").replace("[", "").replace("]", "").replace("'", "")
    #создаем переменную named_arguments, передаём туда параметры kwargs и удаляем/заменяем некоторые символы
    named_arguments = str(kwargs).replace(" ", "").replace("{", "").replace("}", "").replace("'", "").replace(":", "=").replace(",", "&")
    return str(url) + "/" + positional_arguments + "?" + named_arguments

print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))



# Генерация сайта библиотеки

Перед началом работы рекомендуется скачать книги с помощью 
скрипта доступного по ссылке https://github.com/AntonGorynya/lib_parser указав папку загрузки books. Вы можете это сделать с помощью команды ниже
```commandline
> python .\parse_tululu_category.py --dest_folder books
```

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Подготовка к запуску
- Убедитесь в наличие файла **book.json** в котором описываются книги вида.
```commandline
[
    {
        "id": "239",
        "author": "ИВАНОВ Сергей",
        "title": "Алиби",
        "img": "books\\239.jpg",
        "description": "Фантастический детективные рассказ опубликованный в журнале \"Юный техник\", 1991, © 8, С. 30 – 34.OCR В. КузьминSept. 2001Проект \"Старая фантастика\"http://sf.nm.ru",
        "comments": [
            "Детский вариант анекдотов про Шерлока Холмса)",
            "Загадки я люблю.)))",
            "А мне понравилось, люблю, знаете ли, всякие загадочки, головоломочки, кроссвордики, Гимнастика ума, одним словом... \nВо всём можно найти положительные моменты, не разгадал загадку, так хоть гренки научился готовить отменные... :-)",
            "Очень поучительное для ребенка 10 лет."
        ],
        "genres": [
            "Научная фантастика",
            "Прочие Детективы"
        ],
        "book_path": "books\\239. Алиби.txt"
    },
]
```
- переместите обложки книг в папку **media\images** 



### Пример запуска
Для генерации сайта воспользуйтесь командой
```commandline
> python .\render_website.py
```
При необходимости передайте путь то файла **book.json** в ключе `--json_path`

### Доступ к сайту
После запуска скрипта, вы сможете получить доступ к локальной версии сайта, которая находится по умолчанию по адрессу
http://127.0.0.1:5500/pages/index1.html

Или через открытие html страниц в папке **pages** в корне скрипта.

### Пример
Пример сайта можно найти по ссылке
https://antongorynya.github.io/lib_site_generator/pages/index1.html

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

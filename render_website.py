import json
import os
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader
from livereload import Server


BOOKS_PER_PAGE = 10
INDEX_FOLDER = 'pages'

def load_template():
    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template('index template.html')
    return index_template


def rebuild():
    with open('books.json', 'r', encoding="utf8") as file:
        books = json.loads(file.read())
    paged_books = list(chunked(books, BOOKS_PER_PAGE))
    index_template = load_template()
    for page_num, page in enumerate(paged_books):
        path = os.path.join(INDEX_FOLDER, f'index{page_num}.html')
        os.makedirs(INDEX_FOLDER, exist_ok=True)
        with open(path, mode='w', encoding='utf8') as result:
            result.write(index_template.render(books=page))


if __name__ == '__main__':
    server = Server()
    rebuild()
    server.watch('templates/*.html', rebuild)
    server.serve(root='./')

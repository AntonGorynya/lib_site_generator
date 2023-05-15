import argparse
import json
import os
from urllib.request import pathname2url

from jinja2 import Environment, FileSystemLoader
from more_itertools import chunked
from livereload import Server


BOOKS_PER_PAGE = 10
INDEX_FOLDER = 'pages'


def create_parser():
    parser = argparse.ArgumentParser(
        description='generate lib '
    )
    parser.add_argument('--json_path', help='Path to json file', default='books.json')
    return parser


def load_template():
    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template('index template.html')
    return index_template


def rebuild():
    with open(JSON_PATH, 'r', encoding='utf8') as file:
        books_meta = json.load(file)
    for book_meta in books_meta:
        book_meta['img'] = os.path.join('..', 'media', 'images', os.path.split(book_meta['img'])[-1])
        book_meta['img'] = pathname2url(book_meta['img'])
        book_meta['book_path'] = os.path.join('..', 'media', book_meta['book_path'])
        book_meta['book_path'] = pathname2url(book_meta['book_path'])

    chunked_meta = list(chunked(books_meta, BOOKS_PER_PAGE))
    last_page_num = len(chunked_meta)
    index_template = load_template()
    for page_num, page in enumerate(chunked_meta, start=1):
        path = os.path.join(INDEX_FOLDER, f'index{page_num}.html')
        os.makedirs(INDEX_FOLDER, exist_ok=True)
        with open(path, mode='w', encoding='utf8') as result:
            result.write(index_template.render(
                books_meta=page,
                last_page_num=last_page_num,
                page_num=page_num)
            )


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    JSON_PATH = args.json_path

    server = Server()
    rebuild()
    server.watch('templates/*.html', rebuild)
    server.serve(root='./')

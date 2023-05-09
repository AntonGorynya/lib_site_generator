import json
from jinja2 import Environment, FileSystemLoader
from livereload import Server, shell


def load_template():
    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template('index template.html')
    return index_template


def rebuild():
    with open('books.json', 'r', encoding="utf8") as file:
        context = json.loads(file.read())
    index_template = load_template()
    with open('index.html', mode='w', encoding='utf8') as result:
        result.write(index_template.render(books=context))


if __name__ == '__main__':
    server = Server()
    rebuild()

    server.watch('templates/*.html', rebuild)
    server.serve(root='./')





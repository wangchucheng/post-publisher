import yaml

from post import Post


def read_file(file_path, statement_path):
    with open(file_path, 'r', encoding= 'UTF-8') as f:
        whole = f.read().split('---\n', 2)
        content = whole[2]
        
        try:
            config = yaml.safe_load(whole[1])
            title = config['title']
            tags = config['tags']
            categories = config['categories']
            draft = config['draft']
            return Post(title, tags, categories, content, draft)
        except yaml.YAMLError as exc:
            print(exc)
            
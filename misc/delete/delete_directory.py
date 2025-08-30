"""Delete all files in the path."""


def delete_my(fs, path):
    for item in fs.match(path):
        if fs.is_directory(item.id):
            delete_my (fs, item.id)
        fs.delete(item.id)
    fs.delete(path)


def delete_tree(fs, id):
    for item in fs.match(id):
        delete_tree(fs, item.id)
    fs.delete(id)

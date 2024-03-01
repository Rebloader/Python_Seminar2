def get_size(directory):
    size = sum(f.stat().st_size for f in directory.glob('**/*') if f.is_file())
    return size


def bypass_directory(directory):
    results = []
    for item in directory.iterdir():
        if item.is_dir():
            results.append({
                'name': item.name,
                'type': 'directory',
                'parent': str(item.parent),
                'size': get_size(item)
            })
        elif item.is_file():
            results.append({
                'name': item.name,
                'type': 'file',
                'parent': str(item.parent),
                'size': item.stat().st_size
            })
    return results

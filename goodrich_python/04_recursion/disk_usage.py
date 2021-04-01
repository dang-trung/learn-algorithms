import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            total += disk_usage(child_path)
    print(f"{total}: {path}")
    return total

if __name__ == '__main__':
    path = os.path.join('.', 'goodrich_python')
    disk_usage(path)

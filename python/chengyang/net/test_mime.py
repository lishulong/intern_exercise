from pykit import mime


if __name__ == '__main__':
    
    filename = [
        'wo.txt',
        'wo.css',
        'wo.html',
        'wo.doc',
        'wo.c',
        'wo.cpp',
        'wo.pdf',
        'wo.jpg',
        'wo.png',
        'wo.gif',
        'wo.py',
        'wo.bmp',
    ]
    
    for v in filename:
        print mime.get_by_filename(v)

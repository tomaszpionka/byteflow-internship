# File objects
# file read
with open('demo.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    """
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
    
    for line in f:
        print(line, end='')
    """
# File write

with open('test.txt', 'w') as w:
    w.write('Test')
    w.seek(1)
    w.write('R')

with open('demo.txt', 'r') as rf:
    with open('test.txt', 'w') as wf:
        for line in rf:
            wf.write(line)





n = 820
with open('/home/drdos/work/file.PDA', "rb") as f:
    while True:
        data = f.read(n)
        if not data:
            break
        
        filename = str(data[16:32])
        
        x = open(filename, 'wb').write(data)
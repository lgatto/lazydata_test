from lazydata import track

with open(track("/home/lg390/tmp/data/some_data_file.txt"), "r") as f:
    print(f.read())

import time
for i in range(1, 6576, 1):
    print(open('converted/ascii_img' + '{:d}'.format(i).zfill(4) + '.txt', "r").read())
    time.sleep(0.0213)
#0.0299
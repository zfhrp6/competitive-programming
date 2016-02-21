(lambda x:print(':'.join(map(str.zfill,map(str,x),[2,2,2]))))((lambda x:[x//
3600, (x%3600)//60, x%60])(int(input())))
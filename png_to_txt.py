import os
 
def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    files.sort(key=lambda x: int(x[:-4]))
 
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    file.write(name + "\n")
                    break
 
 
def Test():
    dir = r"/home/l/dataset/kaist38/image/stereo_right"
    outfile = "/home/l/right.txt"
    wildcard = ".png"
 
    file = open(outfile, "w")
    if not file:
        print("cannot open the file %s for writing" % outfile)
 
    ListFilesToTxt(dir, file, wildcard, 1)
 
    file.close()
 
if __name__ == '__main__':
    Test()

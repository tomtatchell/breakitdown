with open("testscript.py", "r") as sts:
    data = sts.read()
    with open("stringFromScript.txt", "w") as sfs:
        sfs.write(repr(data))



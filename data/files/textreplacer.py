import os
import re

def replace_string(dname, fname, old, new, pyfilecount):
    fpath = os.path.join(dname, fname)
    with open(fpath) as f:
        s = f.read()

    if re.search(old, s):
        s = s.replace(old, new)
        pyfilecount += 1
        with open(fpath, "w") as f:
            f.write(s)
    
    return pyfilecount

def run_program(dir_path, old, new, searchpattern=None):
    filecount = 0

    for dname, dirs, files in os.walk(dir_path):
        for fname in files:
            if searchpattern is not None:                
                if re.search(searchpattern, fname):
                    filecount = replace_string(dname, fname, old, new, filecount)
            else:
                filecount = replace_string(dname, fname, old, new, filecount)

    return filecount

if __name__ == '__main__':
    # path = r'D:\myCode\GitHub\staging\BI Cloud\adsm-scratchpad\python\abinitio poc\gsutil'
    path = r'D:\myCode\GitHub\staging\BI Cloud'

    # oldstring = 'skyuk-uk'
    # newstring = 'blen-prj'

    # count = run_program(path, oldstring, newstring, searchpattern='.py$')
    # print(str(count))

    # count = 0

    # oldstring = 'sky-uk-'
    # newstring = 'blen-gcs-'
    # count = run_program(path, oldstring, newstring, searchpattern='.py$')
    # print(str(count))

    oldstring = 'http://dcslovtfs02:8080/tfs/projectcollection'
    newstring = ''
    count = run_program(path, oldstring, newstring, searchpattern='.sln$')
    print(str(count))
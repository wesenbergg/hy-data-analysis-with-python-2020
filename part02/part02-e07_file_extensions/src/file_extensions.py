#!/usr/bin/env python3

def file_extensions(filename):
    no_ext = []
    ext_files = {} # key: filu muoto, value: filun nimi
    with open(filename, "r") as f:
        for line in f:
            sliced_file = line.strip("\n").split(".")

            if len(sliced_file) == 1: no_ext.append(sliced_file[0])
            elif len(sliced_file) > 1:
                if sliced_file[-1] in ext_files:
                    ext_files[sliced_file[-1]].append( line.strip("\n") )
                else:
                    ext_files[sliced_file[-1]] = [ line.strip("\n") ]
    #print(no_ext, ext_files)
    return (no_ext, ext_files)

def main():
    no_ext, ext = file_extensions("hy/hy-data-analysis-with-python-2020/part02-e07_file_extensions/src/filenames.txt")
    print(f"{len(no_ext)} files with no extension")
    for e in ext:
        print(e, len(ext[e]))

if __name__ == "__main__":
    main()

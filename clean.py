import os

directory = "/Users/ayafdel/Desktop/subs/aots01"
for filename in os.listdir(directory):
    with open(f'{directory}/{filename}') as input:
        with open(f'{filename[:-4]}',"a") as output:
            sep = ",,"
            for single_line in input:
                if sep in single_line:
                    str = single_line.split(",,")
                    output.write(str[len(str)-1])
                #print(str[len(str) - 1].strip('\n'))
import os

PWD = os.getenv('PWD')
input_dir = PWD +"/aots2"
output_dir = PWD + "/aot_cleaned/s2"
for filename in os.listdir(input_dir):
    with open(f'{input_dir}/{filename}') as input:
        with open(f'{output_dir}/{filename[:-4]}',"a") as output:
            sep = ",,"
            for single_line in input:
                if sep in single_line:
                    str = single_line.split(",,")
                    output.write(str[len(str)-1])
                #print(str[len(str) - 1].strip('\n'))
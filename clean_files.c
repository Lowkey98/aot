with open("aots01/aot01.ass","r") as f:
    sep = ",,"
    for single_line in f:
        if sep in single_line:

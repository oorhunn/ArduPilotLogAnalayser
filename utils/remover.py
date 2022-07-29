import os


with open("37.log", "r") as input:
    with open("temp.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if line starts with substring 'time' then don't write it in temp file
            if line.strip("\n").startswith(myarr):
                output.write(line)

# replace file with original name
os.replace('temp.txt', '37.log')

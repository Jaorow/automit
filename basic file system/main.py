from datetime import datetime
import random as r


def main():
    loops = 5
    fw = open("commits.txt","a")
    f = open("commits.txt","r")
    contents = f.read().splitlines()

    if len(contents) > 1 and check_last(contents[-1].split()):
        start = int(contents[-1].split()[0].strip())
    else:
        fw.write(restart(len(contents)))
        start = 0

    for loop in range(loops):
        start += 1
        status = commit()
        fw.write(f"{start} : {str(datetime.now())} : {status} : {datetime.timestamp(datetime.now())}\n")


def check_last(last):
    last = last[0].strip()
    try:
        int(last)
        return True
    except:
        return False

def restart(len):
    if len == 0:
        return "new file stream started at " + str(datetime.now()) + "\n"
    return ("ERROR 108: filestream restarted due to error in count at " + str(datetime.now())+ "\n")


def commit():
    return r.choice(["PASS","FAIL"])

main()
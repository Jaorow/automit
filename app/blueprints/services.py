"""use for all services!"""
from datetime import datetime
import git

def automit():
    loops = 1
    fw = open("commits.txt","a")
    f = open("commits.txt","r")
    contents = f.read().splitlines()

    if len(contents) > 1 and check_last(contents[-1].split()):
        count = int(contents[-1].split()[0].strip())
    else:
        fw.write(restart(len(contents)))
        count = 0

    for loop in range(loops):
        count += 1
        status = commit(count)
        fw.write(f"{count} : {str(datetime.now())} : {status} : {datetime.timestamp(datetime.now())}\n")
    
    repo = git.Repo('')
    repo.remotes.origin.push()
    print("pushed")

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


def commit(count):
    try:
        repo = git.Repo('')
        with repo.config_writer() as git_config:
            git_config.set_value('user', 'email', 'jamiedunwoodie2002@gmail.com')
            git_config.set_value('user', 'name', 'jaorow')
        repo.index.add(['commits.txt'])
        # print("pass")
        repo.index.commit(f"--AUTOMIT--{count}--")

        return "PASS"
    except:
        print("Whoops something broke")
        return "FAIL"
automit()
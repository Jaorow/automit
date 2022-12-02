import os
import git

my_repo = git.Repo('/Users/jamie/Desktop/BASE/dev/automit')
if my_repo.is_dirty(untracked_files=True):
    print('Changes detected.')
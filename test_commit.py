import os
import git



repo = git.Repo('/Users/jamie/Desktop/BASE/dev/automit/')

print(repo.remotes.origin.push())

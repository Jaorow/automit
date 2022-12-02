import os
import git



repo = git.Repo('/Users/jamie/Desktop/BASE/dev/automit/')

# Provide a list of the files to stage
repo.index.add(['test_commit.py'])
# Provide a commit message
repo.index.commit('testing auto commit.')
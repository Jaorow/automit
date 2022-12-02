to clone a reop

```python
from git import Repo
Repo.clone_from("link_to_repo", "directory_to_clone_into")
```
to start repo in python
```python
my_repo = git.Repo('/Users/jamie/Desktop/BASE/dev/automit')
```

to check if there is changes in repo
```python
if my_repo.is_dirty(untracked_files=True):
    print('Changes detected.')
```

set repo
```python
repo = git.Repo('/Users/jamie/Desktop/BASE/dev/automit')
```


to get diffrences between last commit and this commit
```python
diff = repo.git.diff(repo.head.commit.tree)
print(diff)
```
set username and email to repo
```python
with repo.config_writer() as git_config:
    git_config.set_value('user', 'email', 'jamiedunwoodie2002@gmail.com')
    git_config.set_value('user', 'name', 'jaorow')
```

read username and email from repo
```python
with repo.config_reader() as git_config:
    print(git_config.get_value('user', 'email'))
    print(git_config.get_value('user', 'name'))
```

make a commit
```python
# list of files to commit
repo.index.add(['test_commit.py'])
#commit message
repo.index.commit('testing auto commit.')
```

list remotes for repo
```python
print('Remotes:')
for remote in repo.remotes:
    print(f'- {remote.name} {remote.url}')
```

pull from a remote
```python
print(repo.remotes.origin.pull())
```
push to a remote
```python
print(repo.remotes.origin.push())
```
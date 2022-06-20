
### Handy Python References
| Link          | Description            |
|:---------------|:-----------------------|
|[Python difference between `r+`, `w+` and `a+` in `open()`](https://mkyong.com/python/python-difference-between-r-w-and-a-in-open) | Illustrate Python file modes |
|[Python Escape Characters](https://www.w3schools.com/python/gloss_python_escape_characters.asp) | How to use illegal characters in a Python string |
|[Official Python Documentation](https://docs.python.org/3/) | |
|[W3 Schools Python Tutorial](https://www.w3schools.com/python/default.asp) ||
|[learnpython.org](https://www.learnpython.org/)| |

### Interactive Python, clear terminal screen
```
import os
os.system('clear')
```


### Clone course repository to Raspberry Pi
```
cd /home/pi
git clone https://github.com/dora-lee/seneca-prg550-2022-spring.git
```

### Updating local course repository from GitHub

```
cd /home/pi/seneca-prg550-2022-spring
git pull # update local repo from origin
```

1. If you get merge errors, try one of these commands to reset the state of your local repo
    ```
    git stash # stash changes made to repo files
    git rm --cached -r . # clear git's cache
    git reset --hard HEAD  # reset local HEAD to remote's HEAD
    ```
2. **OR** rename the repo directoy and [`git clone` again above](#clone-course-repository-to-raspberry-pi)
    ```
    mv /home/pi/seneca-prg550-2022-spring /home/pi/seneca-prg550-2022-spring_old
    ```

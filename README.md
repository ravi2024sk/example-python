# Monorepo with python

This repo is setup to build two packages:

a) one with main.py within helloworld folder

b) a zip with google function inside of greet folder


# Commands to reproduce error

install pyenv

install python version 3.12.2 using pyenv

`pyenv install 3.12.2`

initialize pyenv: `eval "($pyenv init -))"`

create python virtual environment

`python -m venv venv`

activate virtual env: `source venv/bin/activate`

run: `docker compose up`


# Error Message

`

**build-1**  **| **stderr:

**build-1**  **| **A distribution for pyarrow could not be resolved for cp312-cp312-linux_x86_64.

**build-1**  **| **Found 1 distribution for pyarrow that do not apply:

**build-1**  **| **1.) The wheel tags for pyarrow 16.0.0 are cp312-cp312-manylinux_2_28_x86_64 which do not match the supported tags of cp312-cp312-linux_x86_64:

**build-1**  **| **cp312-cp312-manylinux2014_x86_64

**build-1**  **| **... 122 more ...

`

# Other things attempted

using complete_platforms:

I attempted to set this complete_platforms variable inside of build file associated with greet folder to: **cp312-cp312-manylinux_2_28_x86_64**

if i use complete_platforms variable it would not want runtime variable. So tried commenting that variable. It complained about missing folder. It looks like I needs some json file but not sure what to put into it. 

Thanks in advance.

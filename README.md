# sd-code-test
Span digital basic code test.

This project contains a program to facilitate the basic code test presented to me by the Span digital hiring team.

# Assumptions: 
1. There is an existing python environment. (Preferably pyhton 3.11)
2. The input file will be a .txt file, but other file types could probably work.

# Setting up a python venv. (This assumes terminal use of OSX or LINUX).
1. `pip install virtualenv`
2. `python<version> -m venv <virtual-environment-name>` 
    <version>=3
    <virtual-environment-name>=sd-code-test-venv
3. `source env/bin/activate`

# Package installation and setup:
This command will install all the required packages (acutally only pytest), in the venv, and run the unit & end-to-end tests.
    `make install`

# Methods of running the program:
1. providing a file as input argument to the application at runtime
    example: `python app/main.py tests/testfiles/input_1.txt`
    useable: `python app/main.py path/to/file/relative/to/project/root`
2. pipe the input file as stdin to the python app
    example: `cat app/test/testfiles/input_1.txt | python app/main.py`
    useable: `cat path/to/file/relative/to/project/root | python app/main.py`
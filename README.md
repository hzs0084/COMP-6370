# COMP-6370
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
The version of Python used to develop the code is 3.10.6

1. The code will run only through the terminal of an IDE. I used the latest version of PyCharm Community Edition [Version: 222.3739.56] at the moment to develop the code.

2. To run the code through the terminal, make sure that the test cases are in the same directory as the main.py

3. Type in "python3 main.py from-spec\valid\0002.input"; This should run the test case that is available in the directory of from-spec\valid\0002.input. This is the only way to test manually through an IDE.

4. The output of the test case should print in the terminal. 

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
The version of Python used to test the code in the Linux terminal is 3.8.10


1. Auto-run.py works in a Unix environment. To ensure that it works in a Unix/Linux terminal. Change the Environment of the code so if you are using PyCharm then go to line separators and if the code was written in a Windows Environment change CRLF and switch it to LF.

2. When in a Unix/Linux terminal, make sure that all the files that have test cases, auto-run.py, and main.py are in the same directory. 

3. To make the script an executable, shebang was used while coding. Use the command "chmod +x (name of your script).py"; this will make it an executable to run with auto-run.py

4. Go to auto-run.py and replace "./instructor-solution" with "./main.py".

5. Type in "python3 auto-run.py", it should run through all the test cases and if it runs into an issue with a specific test case, it will display an error. 


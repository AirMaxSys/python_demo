#!/usr/env python

'''
A website requires the users to input username and password to register. Write a program to check
the validity of password input by users.
Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12

    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    ABd1234@1
'''

import re       # regex search

passwds = [pw for pw in input("pass words:").split(',')]
#print(passwds)

valied_pws = []

for pw in passwds:
    if len(pw) < 6 or len(pw) > 12:
        continue
    else:
        pass
    
    if not re.search("[a-z0-9A-Z]", pw):
        continue
    elif not re.search("[$#@]", pw):
        continue
    else:
        pass
    valied_pws.append(pw)
print(','.join(valied_pws))
    #elif not re.search("[0-9]", pw):
    #    continue
    #elif not re.search("[A-Z]", pw):
    #    continue


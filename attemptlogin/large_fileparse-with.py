#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successlogin = 0 # counter for successes

# open the file for reading
with open("/home/student/mycode22/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            ip=print(line.split(" ")[-1])
        elif "-] Authorization failed" in line:
            successlogin += 1 # this is the same as successlogin = loginfail + 1
print("The number of failed log in attempts is", loginfail, "from ",ip)
print("The number of successful log in attempts is", successlogin)

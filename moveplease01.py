#!/usr/bin/env python3

# Import shutil and os
import shutil
import os

def main():
    #Start out in Home directory
    os.chdir('/home/student/mycode22/')

    #move the file or folder at the path source to the path destination
    shutil.move('raynor.obj', 'ceph_storage/')

    #Prompt for a new name for file
    xname = input('What is the new name for kerrigan.obj? ')

    #Rename the current kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

#Calls main function
main()

"""
This file runs the pulltsv.sh script, verify the data entries. 
"""
import sys
import subprocess
import mysql.connector
from verifyEntries import main as verify

def main():
    #Call script to pull down questions
   subprocess.call("cybermillionaire/util/pulltsv.sh")

    verify()
    
    subprocess.call(["cat",  "cybermillionaire/util/susEntries.txt"])
  
    
    
main()


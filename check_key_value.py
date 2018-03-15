import sys
import string
import re
from color_print import *

def check_double_letter(key):
   alphabets = string.ascii_uppercase
   for letter in alphabets:
       if key.count(letter) > 1:
           print bcolors.FAIL+"ERROR : "+bcolors.ENDC+" THE LETTER \""+letter+"\" is duplicates in : "+key
           sys.exit(0)

def check_key(key, elem):
    check_double_letter(key)
    if ')' in key or '(' in key:
        print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"NO parenthses allowed in element : " + elem
        sys.exit(0)
    if key[len(key)-1].istitle() == False:
        print bcolors.FAIL+"SYNTAX ERROR : "+bcolors.ENDC+"\"" + key+"\""
        sys.exit(0)
    for i, char in enumerate(key):
        if i < len(key) - 1 and (char.istitle() and key[i+1] != '+'):
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"Char must be separated by \'+\'. Error inside : " + elem
            sys.exit(0)
        elif char != '+' and char != '!' and char.istitle() == False:
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"Wrong syntax on element : " + elem
            sys.exit(0)
        elif char== "!" and (key[i+1].istitle()==False):
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC + elem
            sys.exit(0)
        elif char== "+" and (key[i+1].istitle()==False and key[i+1]!='!'):
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC + elem
            sys.exit(0)
        elif char == '+' and (i == 0 or i == len(key)-1):
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"Probleme with last or first char in : " + elem
            sys.exit(0)
    return key

def check_value(value, elem):
    operator = ['+','|', '^']
    par1 = 0
    count = 0
    if value[len(value)-1].istitle() == False and value[len(value)-1] != ")":
        print bcolors.FAIL+"SYNTAX 0 ERROR : "+bcolors.ENDC+"\"" + value+"\""
        sys.exit(0)
    for i, char in enumerate(value):
        if char.istitle():
            if i < len(value) - 1 and value[i+1] not in operator and value[i+1] != ")":
                print bcolors.FAIL+"SYNTAX 1 ERROR : "+bcolors.ENDC+"\"" + value+"\""
                sys.exit(0)
        if char in operator:
             if i < len(value) - 1 and (value[i+1].istitle() == False and value[i+1] != "!"and value[i+1] != "("):
                print bcolors.FAIL+"SYNTAX 2 ERROR : "+bcolors.ENDC+"\"" + value+"\""
                sys.exit(0)
        if char == "!":
            if i < len(value) - 1 and value[i+1].istitle()==False:
                print bcolors.FAIL+"SYNTAX 1 ERROR : "+bcolors.ENDC+"\"" + value+"\""
                sys.exit(0)
        if char == "(":
            if i < len(value) - 1 and value[i+1].istitle() == False:
                print bcolors.FAIL+"SYNTAX 3 ERROR : "+bcolors.ENDC+"\"" + value+"\""
                sys.exit(0)
            par1 = i
            count += 1
        if char == ")":
            if par1 > i or (i < len(value) - 1 and (value[i+1] !="+" and value[i+1] !="|")):
                print bcolors.FAIL+"SYNTAX 4 ERROR : "+bcolors.ENDC+"\"" + value+"\""
                sys.exit(0)
            count += 1
    if (count%2 != 0):
        print bcolors.FAIL+"PLACEMENTS OF PARENTHESES IS INCORECT IN : "+bcolors.ENDC + value
        sys.exit(0)
    return value

def check_equations(BC):
    cpy_BC = BC[:]
    del cpy_BC[-2:]
    equations = {}
    for elem in cpy_BC:
        if elem.count('=>') != 1:
            print "FAIL : Wrong number of \'=>\' in : " + elem
            sys.exit(0)
        if elem.count('<=>') == 1:
            print "FAIL : " +"Can't support if and only if "+ elem
            sys.exit(0)
        value, key = elem.split('=>')
        if not key or not value:
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"No value for the key on element : " + elem
            sys.exit(0)
        key = check_key(key, elem)
        value = check_value(value, elem)
        
        if key in equations:
            if value.replace('!', '') in ''.join(equations[key]):
                print bcolors.FAIL + "Inconsistent rules inside : " + bcolors.ENDC+ value+"=>"+key
                sys.exit(0)
            equations[key].append(value)
        else:
            equations[key] = [value]
    return equations
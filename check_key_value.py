import sys
import re
from color_print import *

def check_key(key, elem):
    if ')' in key or '(' in key:
        print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"NO parenthses allowed in element : " + elem
        sys.exit(0)
    for i, char in enumerate(key):
        if i < len(key) - 1 and (char.istitle() and key[i+1] != '+'):
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"Char must be separated by \'+\'. Error inside : " + elem
            sys.exit(0)
        elif char != '+' and char != '!' and char.istitle() == False:
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"Wrong syntax on element : " + elem
            sys.exit(0)
        elif i < len(key) - 1 and (char == '+' and (key[i-1] == key[i+1])):
            print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"SAME operand : " + elem
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
    return value

def check_equations(BC):
    '''
    Transforme ma liste d'equations en dico avec    key   = le resultat
                                                    value = equation
    '''
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
            print key
            sys.exit(0)
            if value.replace('!', '') in ''.join(equations[key]):
                print bcolors.FAIL + "Inconsistent rules inside : " + bcolors.ENDC+ value+"=>"+key
                sys.exit(0)
            equations[key].append(value)
        else:
            equations[key] = [value]
    return equations
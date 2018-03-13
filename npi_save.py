import sys
import re
from color_print import *

def npi(equations, knowledge):
    res = 0
    var_not = []
    var = []
    tmp_know = []
    ope_stack = []
    op_lst = ['+', '|', '^', '!']
    for i , elem in enumerate(equations):
        if elem in op_lst:
            if elem == "!":
                if equations[i+1] not in knowledge:
                    tmp_know.append(equations[i+1])
                else:
                    var_not.append(equations[i+1])
                    knowledge.remove(equations[i+1])
            else:
                ope_stack.insert(0, elem)
        else:
            var.insert(0, elem)
    if not ope_stack:
        if var[0] in knowledge or var[0] in tmp_know:
            res = 1
    for ope in ope_stack:
        if ope == "|":
            if (var[0] in knowledge or var[0]in tmp_know) or (var[1] in knowledge or var[1]in tmp_know):
                res = 1
        elif ope == "+":
            if (var[0] in knowledge or var[0] in tmp_know) and  (var[1]in knowledge or var[1]in tmp_know):
                res = 1
        elif ope == "^":
            if bool(var[0] in knowledge or var[0] in tmp_know) ^ bool(var[1] in knowledge or var[1]in tmp_know):
                res = 1
        del ope_stack[0]
        del var[:2]
    for elem in var_not:
        knowledge.add(elem)
    return res

def bckw(equations, knowledge, key):
    for elem in equations[key]:
        for i, char in enumerate(elem):
            if char.istitle():
                if char in equations and char != key:###TEST DANS LE CAS OU UN ELEM == LA KEY
                    print "\t",
                    bckw(equations, knowledge, char)
            if i == len(elem) - 1:
                verif = npi(elem, knowledge)
                if verif == 0:
                    for i , char in enumerate(key):
                        if char.istitle() and key[i-1] == "!":
                            knowledge.add(char)
                if verif == 1:
                    for i , char in enumerate(key):
                        if char.istitle() and key[i-1] != "!":
                            knowledge.add(char)

def solve(knowledge, questions, equations):
    knowledge = set(knowledge)
    for elem in equations:
            bckw(equations, knowledge,elem)
    for elem in questions:
        if elem in knowledge:
            print elem + " IS TRUE"
        else:
            print elem + " IS FALSE"
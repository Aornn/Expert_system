import sys
import re
from color_print import *
def solve_npi(postfix, knowledge):
    stack = []
    var_not= []
    tmp_know= []
    for elem in postfix:
        res = 0
        if elem.istitle() or elem[0] == "!":
            if elem[0] == "!":
                if elem[1] in knowledge:
                    var_not.append(elem[1])
                    knowledge.remove(elem[1])
                else:
                    tmp_know.append(elem[1])
                stack.append(elem[1])
            else:
                stack.append(elem)
        else :
            if elem == '|':
                if (stack[len(stack)-2] in knowledge or stack[len(stack)-2] in tmp_know) or (stack[len(stack)-1] in knowledge or stack[len(stack)-1] in tmp_know):
                    res = 1
            elif elem == '+':
                if (stack[len(stack)-2] in knowledge or stack[len(stack)-2] in tmp_know) and (stack[len(stack)-1] in knowledge or stack[len(stack)-1] in tmp_know):
                    res = 1
            elif elem == '^':
                if bool(stack[len(stack)-2] in knowledge or stack[len(stack)-2] in tmp_know) ^ bool(stack[len(stack)-1] in knowledge or stack[len(stack)-1] in tmp_know):
                    res = 1
            del stack[len(stack)-2]
            del stack[len(stack)-1]         
            if res == 1:
                stack.insert(0, '@')
                tmp_know.append('@')
            else:
                stack.append('@')
    if len(postfix) == 1:
        if len(postfix[0]) == 1:
            if postfix[0][0] in knowledge or postfix[0][0] in tmp_know:
                res = 1
        else:
            if postfix[0][1] in knowledge or postfix[0][1] in tmp_know:
                res = 1
    for elem in var_not:
        knowledge.add(elem)
    return res

def npi(exp, knowledge):
    stack = []
    postfix = []
    operator = ['+','|','^']
    operator_dict = {'!':4, '+':3,'|':2, '^':1}
    for i, elem in enumerate(exp):
        if elem.istitle():
            if exp[i-1] == "!":
                postfix.append("!"+elem)
            else:
                postfix.append(elem)
        if elem in operator:
            while len(stack) > 0 and stack[len(stack) - 1] != "(" and (operator_dict[stack[len(stack) - 1]] >= operator_dict[elem]):
                postfix.append(stack.pop())
            stack.append(elem)
        if elem  == "(":
            stack.append(elem)
        if elem == ")":
            while stack[len(stack) - 1] != "(":
                postfix.append(stack.pop())
            stack.pop()
    while stack:
        postfix.append(stack.pop())
    return solve_npi(postfix, knowledge)

def bckw(equations, knowledge, key):   
    for elem in equations[key]:
        ret = 0
        print '{0: <52}'.format(str(''.join(elem)) + "=>" + str(key))
        for i, char in enumerate(elem):
            if char.istitle():
                if char in equations and char != key:
                    bckw(equations, knowledge, char)
            if i == len(elem) - 1:
                verif = npi(elem, knowledge)
                if verif == 0:
                    for i , char in enumerate(key):
                        if char.istitle() and key[i-1] == "!":
                            knowledge.add(char)
                            ret = 1
                if verif == 1:
                    for i , char in enumerate(key):
                        if char.istitle() and key[i-1] != "!":
                            knowledge.add(char)
                            ret = 1
                if ret == 1:
                     print bcolors.OKGREEN+"\t|"+key+" True|"+bcolors.ENDC
                else:
                    print bcolors.FAIL+"\t|"+key+" False|"+bcolors.ENDC

def solve(knowledge, questions, equations):        
    knowledge = set(knowledge)
    print bcolors.OKBLUE+"\t ======================"
    print "\t|=====ALL RESULTS=====|"
    print"\t ======================\n"+bcolors.ENDC
    for elem in equations:
        bckw(equations, knowledge,elem)
        print "___________________________"
    print bcolors.OKBLUE+"\n\t ======================"
    print "\t|===RESULTS REQUESTS===|"
    print"\t ======================\n\n"+bcolors.ENDC
    for elem in questions:
        if elem in knowledge:
            print elem + bcolors.OKGREEN+"\t\t\t IS TRUE"+bcolors.ENDC
        else:
            print elem + bcolors.FAIL+"\t\t\t IS FALSE"+bcolors.ENDC
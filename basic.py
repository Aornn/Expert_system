from sys import *
from color_print import *
from lexer import *
from check_BC import *
from check_key_value import *
from npi import *
import sys
import re

def print_quest_know(knowledge, questions):
    '''
        Print les questions et les faits juste pour avoir un recap' et si jamais une des valeurs est nulle
    '''
    if not questions:
        print bcolors.WARNING+"WARNING : "+bcolors.ENDC+"No question transmitted"
    # else:
    #     print "What the value of",
    #     for elem in questions:
    #         print elem,
    #     print "?\n",
    if not knowledge:
        print bcolors.WARNING+"WARNING : "+bcolors.ENDC+"No knowledge transmitted"
    # else:
    #     print "The value of",
    #     for elem in knowledge:
    #         print elem,
    #     print " = true\n",

'''
TO DO :
    parentheses                                 => OBLIGATOIRE
    Check syntaxe partie gauche de l'equation   => OBLIGATOIRE
    Faire le backward chaining                  => DONE
    Gerer les not                               => DONE 
    AND en conclusions                          => DONE
    Gerer les nots devant parentheses           => BONUS
    NOT in conclusions                          => BONUS
'''

def run():
    if len(argv)  < 2:
        print("No input file")
        sys.exit()
    data = open_file(argv[1])
    BC = lex(data)
    knowledge = identify_by_char(BC, '=')
    questions = identify_by_char(BC, '?')
    equations = check_equations(BC)
    #print_quest_know(knowledge, questions)
    #print "equation :",
    #print equations
    #print "knowledge :",
    #print knowledge
    #print "questions :",
    #print questions
    solve(knowledge, questions, equations)#Pense a retirer BC
run()

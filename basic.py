from sys import *
from color_print import *
from lexer import *
from check_BC import *
from check_key_value import *
from npi import *
import sys
import re

def print_quest_know(knowledge, questions):
    if not questions:
        print bcolors.WARNING+"WARNING : "+bcolors.ENDC+"No question transmitted"
    if not knowledge:
        print bcolors.WARNING+"WARNING : "+bcolors.ENDC+"No knowledge transmitted"

def run():
    if len(argv)  < 2 or len(argv) > 2:
        print("No input file")
        sys.exit()
    data = open_file(argv[1])
    BC = lex(data)
    print" _____                     _         _____           _                             ___ _____" 
    print"|  ___|                   | |       /  ___|         | |                    ____   /   / __  |"
    print"| |____  ___ __   ___ _ __| |_ _____\ `--. _   _ ___| |_ ___ _ __ ___     / __ \ / /| `' / /'"
    print"|  __\ \/ | '_ \ / _ | '__| __|______`--. | | | / __| __/ _ | '_ ` _ \   / / _` / /_| | / /  "
    print"| |___>  <| |_) |  __| |  | |_      /\__/ | |_| \__ | ||  __| | | | | | | | (_| \___  ./ /___"
    print"\____/_/\_| .__/ \___|_|   \__|     \____/ \__, |___/\__\___|_| |_| |_|  \ \__,_|   |_\_____/"
    print"          | |                               __/ |                         \____/             "
    print"          |_|                              |___/  made by rqueverd                           "
    print""
    print""  
    knowledge = identify_by_char(BC, '=')
    questions = identify_by_char(BC, '?')
    equations = check_equations(BC)
    if not equations:
         print bcolors.WARNING+"WARNING : "+bcolors.ENDC+"No equations transmitted"
    print_quest_know(knowledge, questions)
    solve(knowledge, questions, equations)
run()

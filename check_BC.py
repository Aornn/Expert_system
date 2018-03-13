import re
from color_print import *
import sys

def check_position_knowledge_questions(BC, given_char):
    '''
        Check les doublons des questions et des faits et regarde si la position des questions et des faits
        est bonne cad dans l'ordre : equation->faits->question, SI pas cette ordre->erreur (CHECK EFFECTUE 2 FOIS)
    '''
    list_check_1 = [] #questions
    list_check_2 = [] #knowledge
    for elem in BC:
        if re.match("\?[A-Z]*", elem) != None:
           list_check_1.append(elem)
        if re.match("=[A-Z]*", elem) != None:
           list_check_2.append(elem)
    if len(list_check_1) > 1 or len(list_check_2) > 1:
        print bcolors.FAIL+"ERROR : "+bcolors.ENDC+"DOUBLE VALUE IN KNOWLEDGE OR QUESTIONS "
        sys.exit(0)
    else:
        if not re.match("\?[A-Z]*",BC[len(BC)-1]):#Questions
            print bcolors.FAIL+"FAIL : "+bcolors.ENDC+"Questions must be one line lower than knowledge and be the last line"
            print "\t LAST LINE:\'"+BC[len(BC)-1]+"\'",
            sys.exit(0)
        elif not re.match("\=[A-Z]*",BC[len(BC)-2]):#Knowledge
            print bcolors.FAIL+"FAIL : "+bcolors.ENDC+"Knowledge must be one line upper than questions"
            print "\t BAD LINE:\'"+BC[len(BC)-2]+"\'",
            sys.exit(0)


def identify_by_char(BC, given_char):
    '''
        Met dans une liste les questions et les faits
    '''
    return_token = []
    state = 0
    for elem in BC:
        if re.match(re.escape(given_char)+"[A-Z]*", elem) != None:
            if elem.find('>') != -1:
                print bcolors.FAIL+"ERROR: "+bcolors.ENDC+"wrong syntax : \""+elem+"\""
                sys.exit(0)
            elem = str(elem).replace(given_char, '')
            for i, char in enumerate(elem):
                if char.istitle() == False or (i < len(elem) - 1 and char == elem[i+1]):
                    print bcolors.FAIL+"ERROR: "+bcolors.ENDC+"wrong syntax : \""+elem+"\""
                    sys.exit(0)
                return_token.append(char)
            state = 1
    if state == 0:
        print bcolors.FAIL+"ERROR : NO QUESTIONS OR KNOWLEDGE GIVEN"
        sys.exit(0)
    elif given_char == '?':
        check_position_knowledge_questions(BC, given_char)
    return return_token
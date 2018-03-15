import sys
from color_print import *
def open_file(filename):
    data = open(filename, "r").read()
    data = data.replace(' ', '')
    return data

def unify_list(filecontents):
    for i, char in enumerate(filecontents):
        if char == '=' and filecontents[i+1] == '>':
            filecontents[i] = "=>"
            del filecontents[i+1]
        if char == '<' and filecontents[i+1] == '=' and filecontents[i+1] == '>':
            filecontents[i] = "<=>"
            del filecontents[i+1]
            del filecontents[i+2]
    return filecontents

def lex(filecontents):
    BC = []
    tok = ""
    comment = ""
    filecontents = list(filecontents)
    filecontents = unify_list(filecontents)
    if len(filecontents) == 0:
        print "FILE IS EMPTY"
        sys.exit(0)
    if (filecontents[len(filecontents)-1] != "\n"):
        print bcolors.FAIL+"FAIL : "+bcolors.ENDC+"The file must be terminated by \'\\n\'"
        sys.exit(0)
    for i, char in enumerate(filecontents):
        if char == '#' and not comment:
            while (filecontents[i] != '\n') and (i < len(filecontents) -1):
                comment += filecontents[i]
                i += 1
        if char == "\n" or i == len(filecontents):
            tok = tok.replace(comment, '')
            tok = tok.replace('\n','')
            if tok :
                BC.append(tok)
            tok = ""
            comment = ""
        tok += char
    if not BC:
        print "FILE IS EMPTY"
        sys.exit(0)
    return BC
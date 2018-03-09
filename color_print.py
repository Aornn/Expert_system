import re
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# def ask_knowledge(filecontents):
#     return_token = []
#     if not re.search(r"=[A-Z]*[^>]", filecontents):
#         print(bcolors.FAIL + "ERROR : No knowledge in the input file")
#         sys.exit(0)
#     else:
#         tok_knowledge = re.findall(r"=[A-Z]*[^>]", filecontents)
#         tok_knowledge = ''.join(tok_knowledge)
#         tok_knowledge = tok_knowledge.replace('\n','')
#         for elem in tok_knowledge:
#             if elem != '=' and elem.istitle() == False:
#                 print(bcolors.FAIL + "ERROR : Wrong input format")
#                 sys.exit(0)
#         tok_knowledge = tok_knowledge.replace('=','')
#         if not tok_knowledge :
#             print (bcolors.WARNING + "WARNING:"+ bcolors.ENDC+" No knowledge transmitted")
#         for elem in tok_knowledge:
#             return_token.append(elem)
#         print return_token

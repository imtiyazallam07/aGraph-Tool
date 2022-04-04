from setuptools import Command
from color_constant import BOLD_RED


def parse_parameters_single(command):
    command = command.replace(' ', '')
    para = list(map(int, command[command.index('(') + 1:len(command) - 1].split(','))) 
    if len(para) != 2:
        print(BOLD_RED + "Traceback (most recent call last):\n    Required 1 point but found " + str(len(para)) + " parameters")
        return False
    return para 

def parse_parameters_double(command):
    command = command.replace(' ', '')
    command = command[command.index('(') + 1 : len(command) - 1]
    command = command.replace('),(', ') (')
    para = command.split(' ')
    if len(para) != 2:
        print(BOLD_RED + "Traceback (most recent call last):\n    Required 2 point but found " + str(len(para)))
        return False
    p1 = parse_parameters_single(para[0])
    p2 = parse_parameters_single(para[1])
    return [p1, p2]

def parse_parameters_triple(command):
    command = command.replace(' ', '')
    command = command[command.index('(') + 1 : len(command) - 1]
    command = command.replace('),(', ') (')
    para = command.split(' ')
    if len(para) != 3:
        print(BOLD_RED + "Traceback (most recent call last):\n    Required 3 point but found " + str(len(para)))
        return False
    p1 = parse_parameters_single(para[0])
    p2 = parse_parameters_single(para[1])
    p3 = parse_parameters_single(para[2])
    return [p1, p2, p3]

def remove_closable(command):
    s1 = ''
    s2 = ''
    if '/*' in command and '*/' in command:
        strt = command.index('/*')
        end = command.rindex('*/')
        s1 = command[:strt]
        s2 = command[end + 2:]
    elif '/**' in command and '*/' in command:
        strt = command.index('/**')
        end = command.rindex('*/')
        s1 = command[:strt]
        s2 = command[end + 2:]
    elif not '*/' in command:
        print(BOLD_RED +
                  "Traceback (most recent call last):\n    <UnclosedComment> Comment is left unclosed: ")
        return True
    return s1 + s2

def remove_complete(command):
    commentsymbol = ''
    if '#' in command and '//' in command:
        commentsymbol = '#' if command.index('#') < command.index('//') else '//'
    else:
        commentsymbol = '#' if '#' in command else '//'
    command = command[0:command.index(commentsymbol)]
    return command

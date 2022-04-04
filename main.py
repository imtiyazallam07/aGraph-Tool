import parser
from color_constant import *
import graph
import socket
import os
import platform


def main(command=""):
    loop = True
    commands = []
    while loop:
        if command.startswith("from file "):
            commands.append(command)
            command = command.replace("from file ", '')
            loop = False
        else:
            loop = True
        if loop:
            print(BOLD_BLUE + "aGraph-Tool", end="")
            print(BOLD_MAGENTA + " in ", end="")
            print(BOLD_GREEN + os.getlogin() +
                  "@" + socket.gethostname(), end="")
            print(RESET + BOLD + ":", end="")
            print(BOLD_BLUE + NORMAL + "~", end="")
            print(RESET + "$ ", end="")
            command = input(BOLD_CYAN)
        if '/*' in command:
            if parser.remove_closable(command) == True:
                continue
            command = parser.remove_closable(command)
        if '#' in command or '//' in command:
            command = parser.remove_complete(command)
        command = command.lower().strip()
        commands.append(command)
        if command.startswith('point('):
            graph.point(parser.parse_parameters_single(command))
        elif command.startswith('line(('):
            graph.line(parser.parse_parameters_double(command))
        elif command.startswith('midpoint(('):
            graph.midpoint(parser.parse_parameters_double(command))
        elif command.startswith('trisect(('):
            graph.trisect(parser.parse_parameters_double(command))
        elif command.startswith('split(('):
            graph.split(parser.parse_parameters_triple(command))
        elif command.startswith('length(('):
            graph.distance(parser.parse_parameters_double(command))
        elif command.startswith('slope(('):
            graph.slope(parser.parse_parameters_double(command))
        elif command.startswith('perpendicular(('):
            graph.perpendicular(parser.parse_parameters_double(command))
        elif command.startswith('median(('):
            graph.median(parser.parse_parameters_triple(command))
        elif command == 'help':
            help()
        elif command == 'clearhist':
            commands = []
            print('Command history successfully cleared.')
        elif command == 'history' or command == 'hist':
            commands = commands[:-1]
            if len(commands) == 0:
                print("No history")
                continue
            print(commands)
            if commands[0].startswith('from file '):
                print(BOLD_RED + 'Parsing from file doesn\'t show history')
            else:
                for h in commands:
                    print(h)
        elif command == 'clear':
            if(platform.system() == 'Windows'):
                os.system('cls')
            else:
                os.system('clear')
        elif command == 'exit':
            exit(0)
        elif command == '' or command.startswith("#") or command.startswith('//'):
            commands = commands[:-1]
            continue
        else:
            print(BOLD_RED +
                  "Traceback (most recent call last):\n    <UnavailableCommand> Command not found: ", command)


def help():
    print(
        f"""{RESET + BOLD_BLUE}aGraph Tool commands:
{BOLD_GREEN}point{RESET}          : plots a point on graph
    Usage:
        {BOLD_CYAN}point{RESET + BOLD_MAGENTA}(x₁, y₁)
{BOLD_GREEN}line{RESET}           : plots a line on graph
    Usage
        {BOLD_CYAN}line{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}midpoint{RESET}       : Calculates the midpoint and display it on graph
    Usage:
        {BOLD_CYAN}midpoint{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}trisect{RESET}        : trisect the line and plot it on graph
    Usage:
        {BOLD_CYAN}trisect{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}split {RESET}         : split the line into two parts using a point calculated using given ratio and plotted on the graph
    Usage:
        {BOLD_CYAN}split{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂), (m₁, m₂))
{BOLD_GREEN}length {RESET}        : calculates the length of the line segment
    Usage:
        {BOLD_CYAN}length{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}slope  {RESET}        : calculate the slope of the given line segment
    Usage:
        {BOLD_CYAN}slope{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}perpendicular{RESET}  : calculate the slope of the perpendicular of the given line segment
    Usage:
        {BOLD_CYAN}perpendicular{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}median{RESET}         : calculates the point of intersection of medians of a triangle. It also shows the three lines of median
    Usage:
        {BOLD_CYAN}median{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂), (x₃, y₃))
{BOLD_GREEN}help  {RESET}         : shows the help message
    Usage:
        {BOLD_CYAN}help
{BOLD_GREEN}history {RESET}       : displays the command history
    Usage:
        {BOLD_CYAN}history
        {RESET}   OR
        {BOLD_CYAN}hist
{BOLD_GREEN}clearhist {RESET}     : clears the command history
    Usage:
        {BOLD_CYAN}clearhist
{BOLD_GREEN}clear  {RESET}        : clears the terminal
    Usage:
        {BOLD_CYAN}clear
{BOLD_GREEN}exit  {RESET}         : terminates the program
    Usage:
        {BOLD_CYAN}exit
{BOLD_GREEN}comments  {RESET}     : Comments
    Complete line comment:
        Text after # or // are whole line comment and are completely ignored
        Usage example:
            {BOLD_YELLOW}# This is a comment
            {BOLD_YELLOW}// This is also a comment
            {BOLD_CYAN}point{BOLD_MAGENTA}(7, 8) {BOLD_YELLOW}# This is a comment
            {BOLD_CYAN}point{BOLD_MAGENTA}(7, 8) {BOLD_YELLOW}// This is also a comment{RESET}
        In the above lines the comments are ignored and the remaining commands are executed
    Closable comment
        Text inside /* and */ or /** and */ are closable comments
        Usage example:
            {BOLD_YELLOW}/* This is a comment */ {BOLD_CYAN}point{BOLD_MAGENTA}(7, 8)
            {BOLD_YELLOW}/** This is a comment */ {BOLD_CYAN}point{BOLD_MAGENTA}(7, 8){RESET}
        In the above lines the comments are ignored and the remaining commands are executed
""")

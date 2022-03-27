import parser
from color_constant import *
import graph
import socket
import os
import platform


def main():
    command = ""
    while True:
        print(BOLD_BLUE + "aGraph-Tool", end="")
        print(BOLD_MAGENTA + " in ", end="")
        print(BOLD_GREEN + os.getlogin() + "@" + socket.gethostname(), end="")
        print(RESET + BOLD + ":", end="")
        print(BOLD_BLUE + NORMAL + "~", end="")
        print(RESET + "$ ", end="")
        command = input(BOLD_CYAN).lower().strip()
        if command.startswith('point('):
            graph.point(parser.parse_parameters_point(command))
        elif command.startswith('line(('):
            graph.line(parser.parse_parameters_line(command))
        elif command.startswith('midpoint(('):
            graph.midpoint(parser.parse_parameters_line(command))
        elif command.startswith('trisect(('):
            graph.trisect(parser.parse_parameters_line(command))
        elif command.startswith('split(('):
            graph.split(parser.parse_parameters_ratio(command))
        elif command.startswith('length(('):
            graph.distance(parser.parse_parameters_line(command))
        elif command.startswith('slope(('):
            graph.slope(parser.parse_parameters_line(command))
        elif command.startswith('perpendicular(('):
            graph.perpendicular(parser.parse_parameters_line(command))
        elif command == 'help':
            help()
        elif command == 'clear':
            if(platform.system() == 'Windows'):
                os.system('cls')
            else:
                os.system('clear')
        elif command == 'exit':
            break
        else:
            print(
                "Traceback (most recent call last):\n    <UnavailableCommand> Command not found: ", command)


def help():
    print(
        f"""{RESET + BOLD_BLUE}aGraph Tool help:
{BOLD_GREEN}point{RESET}          : plots a point on graph
    Usage:
        {BOLD_CYAN}point{RESET + BOLD_MAGENTA}(x₁, y₁)
{BOLD_GREEN}line{RESET}           : plots a line on graph
    usage
        {BOLD_CYAN}line{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}midpoint{RESET}       : Calculates the midpoint and display it on graph
    Usage:
        {BOLD_CYAN}midpoint{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}trisect{RESET}        : trisect the line and plot it on graph
    Usage:
        {BOLD_CYAN}trisect{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}split {RESET}         : split the line into two parts using a point calculated using given ratio and plotted on the graph
    Usage:
        {BOLD_CYAN}split{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}length {RESET}        : calculates the length of the line segment
    Usage:
        {BOLD_CYAN}length{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}slope  {RESET}        : calculate the slope of the given line segment
    Usage:
        {BOLD_CYAN}slope{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
{BOLD_GREEN}perpendicular{RESET}  : calculate the slope of the perpendicular of the given line segment
    Usage:
        {BOLD_CYAN}perpendicular{RESET + BOLD_MAGENTA}((x₁, y₁), (x₂, y₂))
""")


main()

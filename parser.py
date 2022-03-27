
def parse_parameters_line(command):
    command = command.replace(' ', '')
    command = command[command.index('(') + 1 : len(command) - 1]
    command = command.replace('),(', ') (')
    para = command.split(' ')
    p1 = parse_parameters_point(para[0])
    p2 = parse_parameters_point(para[1])
    return [p1, p2]

def parse_parameters_point(command):
    command = command.replace(' ', '')
    return list(map(int, command[command.index('(') + 1:len(command) - 1].split(',')))
def parse_parameters_ratio(command):
    command = command.replace(' ', '')
    command = command[command.index('(') + 1 : len(command) - 1]
    command = command.replace('),(', ') (')
    para = command.split(' ')
    p1 = parse_parameters_point(para[0])
    p2 = parse_parameters_point(para[1])
    p3 = parse_parameters_point(para[2])
    return [p1, p2, p3]


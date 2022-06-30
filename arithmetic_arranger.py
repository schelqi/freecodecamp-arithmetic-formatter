def arithmetic_arranger(problems_list):
    arranged_problems = ''
    operators = ['+', '-']
    show_result = False

    if len(problems_list) == 2:
        show_result = problems_list[1]

    problems = problems_list[0]

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    if show_result == True:
        line4 = '\n'
    l = list()

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        problem_split = problem.split()
        operator = problem_split[1]
        if operator not in operators:
            return "Error: Operator must be '+' or '-'."
        try:
            operand_up = int(problem_split[0])
            operand_down = int(problem_split[2])

            op1 = len(problem_split[0])
            op2 = len(problem_split[2])

            if op1 > 4 or op2 > 4:
                return 'Error: Numbers cannot be more than four digits.'

            l.append(max(op1, op2))
        except ValueError:
            return 'Error: Numbers must only contain digits.'
    space_len_1 = 2
    space_len_2 = 0
    for i in range(len(problems)):
        problem_split = problems[i].split()
        operator = problem_split[1]
        operand1 = int(problem_split[0])
        operand2 = int(problem_split[2])

        li = l[i]
        line1 += ' ' * space_len_1
        temp = '{operand:%lid}'%li
        line1 += temp.format(operand=operand1)

        line2 += ' ' * space_len_2
        line2 += operator + ' '
        temp = '{operand:%lid}'%li
        line2 += temp.format(operand=operand2)

        line3 += ' ' * space_len_2
        line3 += '-' * (li + 2)


        if show_result == True:
            result = operand1 + operand2 if operator == '+' else operand1 - operand2

            if result < 0 or len(str(result)) > li:
                space_len_1 -= 1
            line4 += ' '*space_len_1

            line4 += temp.format(operand=result)
        space_len_1 = 6
        space_len_2 = 4

    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + line4
    return arranged_problems

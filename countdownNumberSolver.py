def copyWithout(numList, elem):
    answer = []
    for x in numList:
        if x != elem:
            answer.append(x)
    return answer


def countdownNumerSolver(numbers, target):
    answer = {}

    def recursiveSolve(numList, total, solution):
        def add(n, numbers, total, solution):
            recursiveSolve(numbers, total + n, "( " + solution + " + " + str(n) + " )")

        def sub(n, numbers, total, solution):
            recursiveSolve(numbers, total - n, "( " + solution + " - " + str(n) + " )")
            recursiveSolve(numbers, n - total, "( " + str(n) + " - " + solution + " )")

        def mult(n, numbers, total, solution):
            recursiveSolve(numbers, total * n, "( " + solution + " * " + str(n) + " )")

        def div(n, numbers, total, solution):
            if n != 0:
                recursiveSolve(numbers, total / n, "( " + solution + " / " + str(n) + " )")
            if total != 0:
                recursiveSolve(numbers, n / total, "( " + str(n) + " / " + solution + " )")

        # if no more numbers are left, add the solution to the answer hashtable
        if len(numList) == 0:
            if str(total) in answer:
                answer[str(total)].append(solution)
            else:
                answer[str(total)] = [solution]
        # otherwise call every operation for every number in numbers
        else:
            for elem in numList:
                add(elem, copyWithout(numList, elem), total, solution)
                sub(elem, copyWithout(numList, elem), total, solution)
                mult(elem, copyWithout(numList, elem), total, solution)
                div(elem, copyWithout(numList, elem), total, solution)

    for unique in set(numbers):
        recursiveSolve(numList=copyWithout(numbers, unique), total=unique, solution=str(unique))
    if str(target) in answer:
        return {str(target):answer[str(target)]}
    else:
        count = 1
        while True:
            if str(target + count) in answer:
                if str(target - count) in answer:
                    return {str(target + count): set(answer[str(target + count)]),
                            str(target - count): set(answer[str(target - count)])}
                else:
                    return {str(target + count): set(answer[str(target + count)])}
            elif str(target - count) in answer:
                return {str(target - count): set(answer[str(target - count)])}
            count += 1


print(countdownNumerSolver(numbers=[25, 2, 5, 3], target=250))

check_list = [11, 13, 14, 16, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n ==0 for n in check_list):
            return num
    return num

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print ("No answer found")
    else:
        print (solution)

def function_for_test(list_in):
    list_temp = []
    for i in range(len(list_in)):
        if type(list_in[i]) == int:
            list_temp.append(list_in[i])
    return list_temp

def hello_who(name):
    return f'Hello, {name}'


def salary(hours, salary_by_hour):
    k = 2
    return hours * salary_by_hour * k

# def function_name(parameters):
#     //do something

def no_sum(first,second):
    print(first + second)
no_sum(2345,23456)


def no_sum(first , second = int(10)):
    print(first + second)
no_sum(int(input()))
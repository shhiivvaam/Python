# try:
#     num = int(input())
#     print(num)
# except:
#     print("not")

# exception

# n = int("34 6")  # '''value error'''_because of the space bte the no. 
# print(n,type())

# print("enter the no.")
# n = int(input())
# print(n, type(n))

# print("enter the no.")
# try:
#     n = int(input())
#     out = 1 / n
#     print(out)
# except:
#     print("not a valid no.")

# print("enter the no.")
# try:
#     n = int(input())
#     out = 1 / n
#     print(out)
# except Exception as e:
#     print("not a valid no.", e)

# print("enter the no.")
# try:
#     n = int(input())
#     out = 1 / n
#     print(out)
# except (ValueError, ZeroDivisionError):
#     print("not a valid no.", e)

print("enter the no.")
try:
    n = int(input())
    out = 1 / n
    print(out)
except ValueError:
    print("not a valid no.")
except ZeroDivisionError:
    print("not an error")


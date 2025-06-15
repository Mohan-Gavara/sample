a=4
b=0
try:
    print(a/b)
    k=int(input("enter a number:"))
    print(k)

except ZeroDivisionError as e:
    print('hey you got an error :',e)
except ValueError as e:
    print("you enter is wrong:",e)

finally:
    print("Could you enter correctly")
try:
    f=open("functions",'a')
except Exception as e:
    print("error occured",e)
finally:
    print(" thank you for comming")
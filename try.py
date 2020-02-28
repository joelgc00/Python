for i in range (5):
    try:
        print(i / 0)
    except ZeroDivisionError as e:
        print (e,"===> Division by 0 is non allowed, sorry")
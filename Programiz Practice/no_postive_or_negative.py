x = -10

# if, elif, else method
if x > 0:
    print("%0.2f is +ve no" %(x))
elif x < 0:
    print("%0.2f is -ve no" %(x))
else:
    print("%0.2f is zero" %(x))

# nested if method
if x >= 0:
    if x == 0:
        print("%0.2f is zero" %(x))
    else:
        print("%0.2f is +ve no" %(x))
else:
    print("%0.2f is -ve no" %(x))
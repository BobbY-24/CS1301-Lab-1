def countEvenDigits(num1):
    num1  = str(num1)
    newnum = 0
    num2 = "02468"
    for ch in num1:
        for ch1 in num2:
            if ch1 == ch:
                newnum += 1
    return(newnum)

countEvenDigits(1234567890)
            

def calculatePay():
    # This first line is provided for you
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay  = hrs * rate
    Othours = hrs - 40
    OtRate = rate * 1.5

    if hrs < 40:
        print(f"Pay: {pay} ")
    elif hrs >= 40:
        pay = (40 * rate ) + (Othours * OtRate)
        print(f"Pay: {pay} ")
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()

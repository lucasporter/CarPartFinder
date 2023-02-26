import Data as Data
import sys
import time
def main():
    homePage()
    

def homePage():
    print("")
    print("Welcome to Part Finder!\n")
    vehicleYear = input("Please enter your vehicle Year: ")
    vehicleMake = input("Please enter your vehicle Make: ")
    vehicleModel = input("Please enter your vehicle Model: ")
    requestedPart = input("What part are you looking for today: ")
    checkInput(vehicleYear, vehicleMake, vehicleModel)

def checkInput(year, make, model):
    print('Looking for your Car', end="")
    for i in range(5):
        time.sleep(.5)
        sys.stdout.write('.')
        sys.stdout.flush()
    print("")
    if [year, str(make).capitalize(), str(model).capitalize()] in Data.getCarData():
        print("Found your Car!")
    else:
        print("I cant seem to find that car, please check your input and try again\n")
        print("--------------------------------------------------------------------------------------------\n\n")
        homePage()


    
main()

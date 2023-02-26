import csv
def getVehicleInfo():
    vehicleYear = input("Please enter your vehicle Year: ")
    vehicleMake = input("Please enter your vehicle Make: ")
    vehicleModel = input("Please enter your vehicle Model: ")

def getPartInfo():
    requestedPart = input("What part are you looking for today: ")

def getCarData():
    
    with open('CarData/1926-2013.txt', 'r') as file_obj:
        data = []
        for line in file_obj:
            data.append(line)
    print(data[0])
        
        
            


    

getCarData()  


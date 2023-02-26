import csv
def getVehicleInfo():
    vehicleYear = input("Please enter your vehicle Year: ")
    vehicleMake = input("Please enter your vehicle Make: ")
    vehicleModel = input("Please enter your vehicle Model: ")

def getPartInfo():
    requestedPart = input("What part are you looking for today: ")

def getCarData():
    with open('CarData/1926-2023.txt', 'r') as file_obj:
        data = file_obj.read()
        carInfo = data.split("\n")
        cleanCarInfo = []
    for i in range(len(carInfo)):
        str = carInfo[i]
        result = ','.join([s for s in str.split(',') if s])
        cleanCarInfo.append(result)
    for i in range(len(cleanCarInfo)):
        string = cleanCarInfo[i]
        newstring = string.split(',')
        cleanCarInfo[i] = newstring

    print(len(cleanCarInfo))
    print(cleanCarInfo[0:25])
  #  CarMMY = cleanCarInfo.split("\n")
  # CarMMY = [x[0].split(',') for x in cleanCarInfo]


    
    
    
        
        
            


    

getCarData()  


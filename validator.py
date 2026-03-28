import requests

def checkMotTax(registration):
    API_KEY = ""  # TO DO: REPLACE WITH YOUR OWN API KEY
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json",
    }
    
    data = {"registrationNumber": registration}
    
    response = requests.post(url, json=data, headers=headers)
  

    # All possible retreivable data from API, delete those which are not required
    if response.status_code == 200:
        vehicle_data = response.json()
        print(vehicle_data)
        taxStatus = vehicle_data.get("taxStatus")
        motStatus = vehicle_data.get("motStatus") 
        taxDueDate = vehicle_data.get("taxDueDate")
        motExpiryDate = vehicle_data.get("motExpiryDate")
        make = vehicle_data.get("make")
        yearOfManufacture = vehicle_data.get("yearOfManufacture")
        engineCapacity = vehicle_data.get("engineCapacity")
        co2Emissions = vehicle_data.get("co2Emissions")
        fuelType = vehicle_data.get("fuelType")
        markedForExport = vehicle_data.get("markedForExport")
        colour = vehicle_data.get("colour")
        typeApproval = vehicle_data.get("typeApproval")
        dateOfLastV5CIssued = vehicle_data.get("dateOfLastV5CIssued")
        wheelplan = vehicle_data.get("wheelplan")
        monthOfFirstRegistration = vehicle_data.get("monthOfFirstRegistration")

        return taxStatus, taxDueDate, motStatus, motExpiryDate
        #make, yearOfManufacture, engineCapacity, co2Emissions, fuelType, markedForExport, colour, dateOfLastV5CIssued, monthOfFirstRegistration
    else:
        return None, None, None, None
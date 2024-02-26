"""
problem1.py
Chiara A
02/26/2024
This program inputs the temperature in degree celcius and outputs the atmospheric pressure at that temperature. 
"""

#User inputs the specific temperature. 
water_boil= int(input("What is the tempature in °C when water begins to boil?: "))

#formula to calculate atmospheric pressure with the variable of boiling water. 
atmospheric_pressure= 5 * water_boil - 400

print("The atmospheric pressure in kPa is", atmospheric_pressure)

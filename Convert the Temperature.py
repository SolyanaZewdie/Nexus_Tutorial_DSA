class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32.0
        return [kelvin, fahrenheit]

if __name__ == "__main__":
  
    celsius_input = float(input("Enter temperature in Celsius: "))
    sol = Solution() 
    result = sol.convertTemperature(celsius_input)
    print("Kelvin", result[0]) 
    print("Fahrenheit", result[1]) 

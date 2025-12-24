# function which prints temperature in kelvin and fahrenheit scale .
# Input : given in celsius scale

def temperature(celsius):
    kelvin =  celsius+273
    fahrenheit = (9*celsius+160)/5
    print(f"Temperature in Kelvin: {kelvin}")
    print(f"Temperature in Fahrenheit: {fahrenheit}")
temperature(25)
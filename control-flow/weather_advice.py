"""
This script will ask the user about the current weather
conditions and provide clothing recommendations based on the input.
This task aims to demonstrate the
use of if , elif , and else statements to make decisions in a program
"""

"""Ask the user to input the current weather from a predefined set of conditions: sunny , rainy ,
or cold """

weather = input(" What is the whether like today ((example. sunny/rainy/cold))?").strip().lower()



""" Provide Clothing Recommendations and Print the clothing
    recommendation based on the weather condition provided by the user."""

if weather == "sunny":
    print("recommend: Wear a t-shirt and sunglasses")
elif weather == "rainy":
    print("recommend: Don't forget your umbrella and a raincoat")
elif weather == "cold":
    print("recommend: Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for this weather")

    



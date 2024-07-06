"""Calculate how old the user will be in the year 2050. 
    To keep calculations simple, assume the current
    year is 2023. Therefore, you need to add 27 years to the user’s current age.
"""
#Prompt the user to input their current age with the question: “How old are you? ”.

age = int(input ("How old are you"))

futureyear = 2050

currentyear = 2023

futureage = ((futureyear - currentyear) + age)

print (f"in {futureyear} you will be) {futureage} old")

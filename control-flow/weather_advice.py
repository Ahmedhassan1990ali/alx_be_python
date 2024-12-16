weather_input = input("What's the weather like today? (sunny/rainy/cold):")
if weather_input == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif weather_input == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
elif weather_input == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."
print (recommendation)
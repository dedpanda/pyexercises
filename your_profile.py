def buildprofile():
	profile = {}
	name = input("Please enter your name: ")
	profile["name"] = str(name)
	height = input("Please enter your height: ")
	profile["height"] = float(height)
	favcol = input("Please enter your favorite color/colour: ")
	profile["favorite color"] = str(favcol)
	author = input("Please enter your favorite author: ")
	profile["favorite author"] = str(author)
	print("")
	print("Based on the information I have collected from you, I have built your profile:")
	print("")
	print("Name: " + profile['name'])
	print("Height: " + str(profile['height']))
	print("Favorite Color: " + profile['favorite color'])
	print("Favorite Author: " + profile['favorite author'])
	print("")
	print("Your profile in python dictionary mode:")
	return profile

# Assignment 10.1
# Lily Faris
# Your Own Class

class Monster:
    monster = {}
# initializing the monster dictionary to be used throughout the class
    def __init__(self, name, monster_dict={}):
        self.name = str(name)
# converting the required name parameter into a string 
        self.monster_dict = monster_dict
# taking in init parameters and making them accessible in other functions    
        self.monster[self.name] = self.monster_dict
# setting the monsters name as the key to the dictionary of body parts within the dictionary 

    def set_arms(self, num_arms, num_fingers=0):
# taking in parameters to set the amount of apendages that the monster may have 
        self.monster_dict['arms'] = num_arms
        self.monster_dict['fingers'] = num_fingers
# then loading that information into the dictionary that sorts those values with the appropriate key

    def set_legs(self, num_legs):
        self.monster_dict['legs'] = num_legs
# taking in a parameter to set the amount of apendages that the monster may have
# then loading that information into the dictionary that sorts those values with the appropriate key

    def set_mouth(self, num_mouths, num_teeth=0):
        self.monster_dict['mouth(s)'] = num_mouths
# taking in parameters to set the amount of apendages that the monster may have
        self.monster_dict['teeth'] = num_teeth
# then loading that information into the dictionary that sorts those values with the appropriate key
    
    def run(self):
# since the monster_dict parameter is referenced so specifically, I put the code into a try, except statement 
        try:
            if self.monster[self.name]['legs'] == 0:
# using the monster dictionary to check how many legs the monster has, if that number is 0, the monster can't run
                return (f"{self.name} cannot run because they have no legs ):")
            if self.monster[self.name]['legs'] == 1:
# using the monster dictionary to check how many legs the monster has, if that number is 1, a unique string is returned   
                return (f"{self.name} can't really run but they're hopping really fast!") 
            else:
                return (f"Woah! look at {self.name} go! with {self.monster[self.name]['legs']} legs no wonder they move so fast.")
# if there is an integer value in the appropriate value spot of the dictionary that is not 0 or 1, a unique string is returned
        except:
            return (f"Error: {self.name} cannot run ):")
# if there is an issue with the monster dictionary, a generalized error string is returned

    def eat(self, food=""):
        self.food = food
# taking in the parameter of a food string
        try:
            if self.monster[self.name]['mouth(s)'] == 0:
                return (f"{self.name} cannot eat because they have no mouth")
# using the monster dictionary to check how many mouths the monster has, if that number is 0, the monster can't eat
            if self.monster[self.name]['teeth'] == 0:
                return (f"{self.name} cannot eat because they have no teeth")
# using the monster dictionary to check how many teeth the monster has, if that number is 0, the monster can't eat
            if self.monster[self.name]['teeth'] == 1:
                return (f"{self.name} cannot really eat {self.food} because they only have 1 tooth!")   
# using the monster dictionary to check how many teeth the monster has, if that number is 1, a unique string is returned
            if self.food == "":
                return (f"{self.name} is hungry but there is no food")
# if the optional of food is left blank, a string is returned describing that the monster has no food
            else:
                return (f"Yummy! {self.name} loves {self.food}!")
# otherwise, if there is no error, the monster "eats" and a unique string is returned 
        except:
            return (f"{self.name} cannot eat because they have no mouth")
# if there is an issue with the monster dictionary, a generalized error string is returned

    def knit(self, project=""):
        self.project = project
# taking in the parameter of what the user will ask the monster to knit
        skillset = ["scarf", "sweater", "gloves", "socks"]
# creating a list of set options for what that project can be 
        self.project = (str(self.project).lower()).strip()
# In case the user inputs a string value that is in the skillset but doesn't match it exactly, I make the parameter lowercase and strip it 
        try:
            if self.project not in skillset:
                return (f"{self.name} doesn't know how to make a {self.project} ):")
# first, I check to see if the project parameter isn't in the monsters skillset and return a unique string
            if self.monster[self.name]['arms'] == 0:
                return (f"{self.name} cannot knit a {self.project} because they have no arms ):")
# then I check to see if the monster has 0 arms and if they do, a unique string is returned
            if self.monster[self.name]['fingers'] == 0:
                return (f"{self.name} made a {self.project} but it's pretty bad because they have no fingers ):")
# using the monster dictionary to check how many fingers the monster has, if that number is 0, a unique string is returned
            else:
                if self.monster[self.name]['fingers'] > 1:
                    return (f"Great job {self.name}! That is a beautiful {self.project}, with {self.monster[self.name]['fingers']} fingers you're a natural")
# using the monster dictionary to check how many fingers the monster has, if that number is greater than 1, a unique string is returned                
                else:
                    return (f"Yikes, with only {self.monster[self.name]['fingers']} fingers knitting might not be for you")
# if everything else is in order and no error is thrown, a unique message is returned referencing the information that affects the knit function        
        except:
            return (f"Error: {self.name} cannot knit a {self.project} ):")
# if there is an issue with the monster dictionary, a generalized error string is returned

    def get_name(self):
        return (f"Your monster's name is {self.name}")
# Using the name data variable that was set as a required parameter in the __init__ function to return a string that tells the user the monster's name

    def get_arms(self):
        return (f"Your monster has {self.monster[self.name]['arms']} arms and {self.monster[self.name]['fingers']} fingers")
# using the monster dictionary to return the arm and finger data in a user-friendly string

    def get_legs(self):
        return (f"Your monster has {self.monster[self.name]['legs']} legs")
# using the monster dictionary to return the leg data in a user-friendly string

    def get_mouth(self):
        return (f"Your monster has {self.num_mouths} mouths and {self.num_teeth} teeth")
# using the monster dictionary to return the mouth and teeth data in a user-friendly string

    def __str__(self):
        self.monster_str += (f"{self.name} has")
# first, I initialize a string that starts with referencing the monster by name 
        keys = list(self.monster_dict.keys())
# then I make a list of keys so that I can know when the last value is added to the string and finish it grammatically how I want 
        for i in self.monster_dict:
            if i == keys[-1]:
                self.monster_str += (f" and {self.monster_dict[i]} {i}.")
# if the value is paired with the last key in the list and it is the last to be added to the string, the string returned reflects that by finishing the sentence
            else:
                self.monster_str += (f" {self.monster_dict[i]} {i},")
# otherwise, each body part is added to a the string in a user-friendly list 
        return str(self.monster_str)


def main():
    jeremy = Monster("Jeremy")
# here, I am creating an instance of the Monster class and giving it a name, "jeremy"
    print(jeremy.run())
# I then use the run function to see what my monster can do 
    jeremy.set_legs(8)
# Since the monster has no legs, I get an error message and use the set_legs function to help jeremy run
    print(jeremy.run())
# I then go back to the run function and let jeremy use his legs

    jeremy.set_mouth(1)
# I use the set function to give jeremy 1 mouth
    print(jeremy.eat("human flesh"))
# since I gave jeremy a mouth and not teeth, I get another error so I go back and use the set_mouth function, throwing in another parameter
    jeremy.set_mouth(1,1)
# I then use the eat function for a final time and let jeremy eat 
    print(jeremy.eat("human flesh"))

    print(jeremy.knit("sweater"))
# similar to the eat function I use the knit function to see if jeremy can knit 
# since jeremy has no arms, he cannot and I use the set function to give him arms and fingers
    jeremy.set_arms(9,7)
# finally, jeremy can knit a sweater
    print(jeremy.knit("sweater"))

# I use my __str__ function to print jeremy's anatomy details after all his work
    print(str(jeremy))



if __name__ == "__main__":
    main()

__name__ = "__main__"
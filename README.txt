DESCRIPTION OF THE CLASS
The purpose of the class is for the user to build a “monster” with a name varying amounts of legs, mouths, teeth, arms, and fingers. With different amounts and variations of each body part, the monster has a different set of skills and capabilities related to running, eating, and knitting.  

DESCRIPTION OF CLASS/DATA VARIABLES 
Monster is a dictionary that contains one key, value pair that contains the name of the monster, and the dictionary of the monster’s body parts. 
Skillset is a list of strings that are the different “projects” that the monster is able to knit. If the parameter for the knit function isn’t in the list, the monster can’t knit it and an error message is returned. 
Keys is a list of body parts that are contained in the monster_dict; the keys to the numerical values of how many of each body part the monster has.
Name is a parameter of the __init__ function and is used throughout the class in print messages to refer to the monster. 
monster _dict is a dictionary of key, value pairs that contain the string description of a body part and an integer value of the count of that body part. 
food is a string parameter for the eat class, the user chooses what the monster eats and it is referenced in the returned message.
Project is a string parameter for the knit class, the user chooses what they want the monster to knit and it is referenced in the returned message
monster _str is the output of the __str__ class. It uses the monster dictionaries to organize the number of body parts and return the monster’s information in a user-friendly string. 

DESCRIPTION OF METHODS
The init function takes in a name and a potential dictionary of body parts. If the dictionary parameter is empty, the monster is unable to perform any of the activity functions. 
The set_arms function takes in two parameters, each integers, one optional and the other not. The num_arms parameter is required to run the function and the user can choose any number of arms for the monster to have. The num_fingers parameter is optional and although it may affect how the monster can interact with some of the later functions, 0 fingers is acceptable. 
The set_legs function allows the user to choose the amount of legs that monster has, with no limit, taking in only one integer parameter. Whether or not the monster has legs affects whether or not it can perform the other functions.
The set_mouth function, like the set_arms function takes in two parameters, both integers, one optional and one not. The required parameter to run the function is a number of mouths for the monster to have. The optional parameter is a number of teeth. Similar to all the set_bodypart functions, the mouth/ teeth count of the monster affects how it can interact with later functions.
All of the activity functions are within a try/ except statement in case the monster_dict is empty, an appropriate error message is returned. The run function is related to the amount of legs that the monster has been given. If the monster has 0 legs, it can’t run and the user is told that. If the monster has one leg, a message is returned describing its hop.
The eat function is related to the number of mouths and teeth that the monster has. This function takes in only one parameter: a food string. If the monster has any number of mouths > 0, they can eat but if the number of teeth they have is 0 or 1, a message is returned telling the user they can’t eat. 
The knit function includes a short list of things the monster knows how to knit and takes in only one parameter that is a string of what the monster will knit. If the parameter isn’t in the monster’s limited skillset, the user receives an error message. This function is related to the number of arms and fingers that the monster has, if the monster has no arms, they can’t knit and if the monster has no fingers, they struggle; the appropriate messages are returned in these instances. 
The get_name, get_arms, get_legs, and get_mouth functions all return a string that tells the user how much of each body part they have at that moment. If the dictionary is empty, there is an error. 
Finally, the __str__ function uses a for loop to collect the data into a string. This function returns a sentence describing the monster to the user.
 

# DEMO PROGRAM DOCUMENTATION #

DESCRIPTION OF DEMO PROGRAM
In the demo program, I create a monster with the name Jeremy by calling the Monster class. Next, I see if Jeremy can run and since he can’t I give him 8 legs and see again if he can run. Since he then has legs, I see a message describing how fast he can run with 8 legs. 
Next, I give Jeremy one mouth and use the eat function to see if he can eat human flesh. Since he has no teeth, I get a message telling me just that before I use the set function and give him one tooth. Since he only has one tooth, I get a message saying jeremy is struggling to eat his human flesh and since I don’t want jeremy to go on a murderous rampage, I stop there. 
Then I tell Jeremy to knit a sweater but since I haven’t yet given him any arms or fingers, I get a message saying he can’t. I use the set function to give him 9 arms and 7 fingers before asking him to knit a sweater again. I then get a message saying Jeremy has knit a great sweater. 
Finally, I print out a sentence of Jeremy's full anatomy with everything I’ve added along the way. 

DEMO INSTRUCTIONS
To run the demo program all the user has to do is customize the parameters to play with the outcomes. Each function has different outcomes for different numbers of body parts.

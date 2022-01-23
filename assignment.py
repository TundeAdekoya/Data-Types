#Join the items of this list to a string sentence. Print the result on the terminal. 
my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
ans1 = " ".join(my_list)
print(ans1)

#Change the value of True in this list to False. Print the result on the terminal
new_list = ['this', "brown", 55, "oxen", True, 0.85]
new_list[4] = False
print(new_list)

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Expected_Output = ['Green', 'White', 'Black'] 
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
ans3 = Sample_List[1:4]
print(ans3)

#Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
favourite_color = ['Orange', 'Purple', 'Indigo']
ans4 = color_list + favourite_color
print(ans4)


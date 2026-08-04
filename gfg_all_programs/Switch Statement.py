# Given a number, you have to use a switch statement to return "One" if the given number is equal to 1, 
# "Two" if the number is 2 and so on till 9 ("Nine") else return "Unknown"(without quotes). 

def utility(number):
    switch = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    return switch.get(number, "Unknown")

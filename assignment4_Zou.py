#l:
def subway_fare(number_swipes = 0, total = 0):
    user_swipes = int(input("How many times did you swipe your card to use the MTA this week? "))
    if user_swipes < 13:
        total = user_swipes * 2.90 
    else:
        total = 13 * 2.90
    return f"You spent ${total:.2f} this week"
print(subway_fare())
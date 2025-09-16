"""
Write the program "99 Bottles of Beer on the Wall" 
using a while loop. Be mindful to change the word 'bottles' to 'bottle' when down to the last one.
You must do the full 99 bottles; the sample shows the last 3 verses.
"""
count = 100
while count > 0:
    if count == 1:
        print("1 bottles of beer on the wall")
        print("1 bottles of beer")
    else:
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer")
    print("Take one down, pass it around")
    count -= 1
    if count == 1:
        print("1 bottle of beer on the wall")
    elif count == 0:
        print("no more bottles of beer on the wall")
    else:
        print(f"{count} bottles of beer on the wall")
print("Assignment 2")


print("Exercise 1: ")
print("")

list1 = [54, 76, 2, 4, 98, 100]

int1_1 = int(input("Input the first integer: "))
int1_2 = int(input("Input the second integer: "))

for i in list1:
    if int1_1 <= i <= int1_2:
        print(i)


print("")
print("Exercise 2: ")
print("")


names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

while True:

    letter = input("Input any letter or 'q' to quit: ")

    if letter.lower() == "q":
        break

    for j in names:
        if letter in j.lower():
            print(j) 


print("")
print("Exercise 3: ")    
print("")


numbers = [-12, 4, 12, 25, 67]

while True:

    num_input = int(input("Input a number to add to list or -99 to stop: "))

    if num_input == -99:
        break

    else:
        numbers.append(num_input)
        numbers.sort()

        print("")
        print(f"{numbers} Is the updated list")    
        print("")


print("")
print("Exercise 4: ")
print("")


words = ("Is this the real life? Is this just fantasy? Caught in a landslide, "
         "no escape from reality Open your eyes, look up to the skies and see I'm just "
         "a poor boy, I need no sympathy Because I'm easy come, easy go, little high, "
         "little low Any way the wind blows doesn't really matter to me, to me Mama, "
         "just killed a man Put a gun against his head, pulled my trigger, now he's "
         "dead Mama, life had just begun But now I've gone and thrown it all away Mama, "
         "ooh, didn't mean to make you cry If I'm not back again this time tomorrow "
         "Carry on, carry on as if nothing really matters Too late, my time has come "
         "Sends shivers down my spine, body's aching all the time Goodbye, everybody, "
         "I've got to go Gotta leave you all behind and face the truth Mama, ooh (any "
         "way the wind blows) I don't wanna die I sometimes wish I'd never been born at "
         "all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do "
         "the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo) "
         "Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I'm just a poor "
         "boy, nobody loves me He's just a poor boy from a poor family Spare him his "
         "life from this monstrosity.")

word_list = words.split()

int4_1 = int(input("Input the first index: "))
int4_2 = int(input("Input the second index: "))

if 0 <= int4_1 < int4_2 <= len(word_list):

    word_slice = word_list[int4_1:int4_2]

    print(f"{word_slice} Is the sliced word/s")    
else:
    print("Invalid indices. Please try again.")
    
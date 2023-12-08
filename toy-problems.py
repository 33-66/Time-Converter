    # onvert_to_24_hour

def convert_to_24_hour(hour, minute, period):
    # This function converts a given time in 12-hour format to 24-hour format.
    # Check if the period is "pm" and the hour is not 12
    if period == "pm" and hour != 12:
        # If so, add 12 to the hour
        hour += 12
    # Check if the period is "am" and the hour is 12
    elif period == "am" and hour == 12:
        # If so, change the hour to 0
        hour = 0
    # u can use print to see the changes
    # print(f"{hour:02d}{minute:02d}")
    return f"{hour:02d}{minute:02d}"


convert_to_24_hour(8, 00, "pm")
# We  are using :02d this to make sure the output of the hours is to 2digits and minutes 2digits  so if hour an minutes are single digits they are formatted into two digits
# num = 5
# print(f"{num:02d}")

    #    two_positive

def two_positive(a, b, c):
    # count the number of positive numbers
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1

    # return True if exactly two positive numbers found, False otherwise
    return count == 2


# U CAN confirm the code by uncommenting this
#  print (two_positive(1,2,3))
   
    #   consonant count

def solve(word):
    # so we group the vowels using set
    vowels = set("aeiou")
    # to keep truck of the  sum of consonantswe  set a variable
    max_sum = 0

    # Iterate over the consonant substrings
    for i in range(len(word)):
        # first loop ,loops over each character in the word checking if its a vowel then loops to the nxt if its a vowel
        if word[i] in vowels:
            continue
        # if its a consonant it will continue to the next loop
        sum = 0
        # sum accumulates the sum of the consonants
        for j in range(i, len(word)):
            if word[j] not in vowels:
                # using ord() we add the consonants  and break when  a  vowel is encountered
                # the ord() used to change alphabetical characters to integers  rep
                # Therefore when u change like b which is 2 -1 = 1 so we add 1  to get actual position
                sum += ord(word[j]) - ord("a") + 1
            else:
                break
            # Then we update  the max_sum
        max_sum = max(max_sum, sum)

    return max_sum


print(solve("money"))
# the ord( ) explained further
# print(ord("s")-ord("a") +1 )
# i can see we used the big O(n**2)

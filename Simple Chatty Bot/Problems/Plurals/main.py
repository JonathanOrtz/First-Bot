number = int(input())
word = input()

# write a condition for plurals
if number == 0 or number> 1:
    a = word + 's'
    print(number, a)
if number == 1:
    print(number, word)
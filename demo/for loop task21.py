

str='Hello 123 World. Have a great 1 day ahead ? 12 njk adsc l lll . % 12'




# character=0
# Digit=0
# Special_char_count=0

# for c in range(len(str)):
#     character+=str[c].isalpha()
#     Digit+=str[c].isdigit()
#     Special_char_count=c-(character+Digit)
#     # print(c)




character=sum(c.isalpha() for c in str)
Digit=sum(c.isdigit() for c in str)
Special_char_count=len(str)-(character+Digit)


print(character)
print(Digit)
print(Special_char_count)






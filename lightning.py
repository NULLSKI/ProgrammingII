print('A program to calculate how far away a lightning strike was based on the thunder.')
t = float(input('How long after the flash did the thunder start?(seconds):'))
d =t*1100
m =d/5280
print ('The lightning was approximately {} miles away').format(m)

# width = 30
#
# print('Abir Yusuf'.ljust(width))
# print("Abir Yusuf".rjust(width))
# print("Abir Yusuf".center(width))

c = 'A'
loop = 5
# for i in range(loop):
#     print(c * i)
for i in range(loop):
    print((c*i).rjust(loop - 1) +c+(c*i).ljust(loop - 1))
#Top Pillars
for i in range(loop+1):
    print((c*loop).center(loop*2)+(c*loop).center(loop*6))

#Middle Belt
for i in range((loop+1)//2):
    print((c*loop*5).center(loop*6))

for i in range(loop+1):
    print((c*loop).center(loop*2)+(c*loop).center(loop*6))

#Bottom Cone
for i in range(loop):
    print(((c*(loop-i-1)).rjust(loop)+c+(c*(loop-i-1)).ljust(loop)).rjust(loop*6))
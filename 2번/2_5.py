print("5-1)")
for i in range(7, 0, -2):
    print(' '* ((7-i) // 2) + '*' *i)

print("5-2)")
for i in range(1, 8):
    if i <= 4:
        stars = 8 - (i - 1) * 2
    else:       
        stars = 2 * (i - 4) + 2
    padding = (8 - stars) // 2
    print(' ' * padding + '*' * stars + ' ' * padding)

print("5-3)")
for i in range(1, 6):
    if i == 1 or i == 5: 
        print('*' * 10)
    else: 
        print('*' + ' ' * 8 + '*')
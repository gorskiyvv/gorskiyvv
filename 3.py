
print('Вітаємо в рулетці!')
import random
 
s = True
 
r = [0, 0, 0, 0, 0, 1]
 
while s:
    x = random.choice(r)
    if x == 1:
        s = False
        print('Вбитий!')
    else:
        print('Живий!')


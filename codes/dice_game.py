import codes.dice2

num=input('4,6,8,12,20, which one?:')
my_dice=codes.dice2.Dice(num)
cpu_dice=codes.dice2.Dice(num)

my_pip=my_dice.shoot()
cpu_pip=cpu_dice.shoot()

print('CPU:'+str(cpu_pip)+'you:'+str(my_pip))

if my_pip > cpu_pip:
    print('congrats. Yon win!')
elif my_pip < cpu_pip:
    print('too bad. You lost!')
else:
    print('tied')
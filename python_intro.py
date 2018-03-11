print('Hello, Django girls!')
if 3>2:
    print('Funguje to!')
if 5>2:
    print('5 je vacsie ako 2')
else:
    print('5 nie je vacsie ako 2')
name='Sonja'
if name == 'Ola':
    print('Ahoj Ola!')
elif name == 'Sonja':
    print ('Ahoj Sonja!')
else:
    print('Ahoj neznama!')
volume = 57
if volume < 20:
    print('It\'s kinda quiet.')
elif 20 <= volume < 40:
    print ('It\'s nice for background music.')
elif 40 <= volume < 60:
    print('Perfect, I can hear all the details.')
elif 60 <= volume < 80:
    print('Nice for parties.')
elif 80 <= volume < 100:
    print('A bit loud!')
else:
    print('My ears are hurting!:(')
#Change the volume if it's too loud or too quiet
if volume > 20 or volume < 80:
    volume = 50
    print('That\'s better!')
def hi():
    print ('Ahoj!')
    print ('Ako sa mas?')
hi()
def hi(meno):
    if meno == 'Wawa':
        print('Ahoj Wawa!')
    elif meno == 'Sonja':
        print('Ahoj Sonja!')
    else:
        print('Ahoj neznama!')

hi('Wawa')

def hi(meno):
    print('Ahoj ' + meno + '!')

hi('Katka')

dievcata = ['Katka', 'Monika', 'Zuzka', 'Ola', 'Ty']

for meno in dievcata:
    hi(meno)
    print('Dalsie dievca')

for i in range(1,6):
    print(i)





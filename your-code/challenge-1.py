import inflect
from word2number import w2n
inf = inflect.engine()


print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')


a = w2n.word_to_num(input('Please choose your first number (zero to five): '))
b = input('What do you want to do? plus or minus: ')
c = w2n.word_to_num(input('Please choose your second number (zero to five): '))


if (b == 'minus') : 
    print(str(inf.number_to_words(a))+' '+b+' '+str(inf.number_to_words(c))+ ' equals '+str(inf.number_to_words(a-c)))

elif (b == 'plus') : 
    print(str(inf.number_to_words(a))+' '+b+' '+str(inf.number_to_words(c))+' equals '+str(inf.number_to_words(a+c)))

else : print('Error, non valid opperator')



print("Thanks for using this calculator, goodbye :)")

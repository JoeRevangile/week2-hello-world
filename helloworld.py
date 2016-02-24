# Programmer: Joe Revangile
######### PROGRAMMING INSTRUCTIONS #######################
# write a program that:                                  #
# 1. greets the user in English                          #
# 2. asks the user to choose from 1 of 3 spoken languages#
#    (pick your favorite languages!)                     #
# 3. displays the greeting in the chosen language        #
# 4. exits                                               #
##########################################################
# Var Declarations
engLang = ('English')
spnLang = 'Spanish'
frLang = 'French'
# Greetings and Asking User to Choose favLang
print('Hello There!')
print('Please choose your favorite language between English, Spanish, or French.\n')
print(' Please note: the language types are case sensative... for now...')
# Taking input from user and assigning it to favLang variable
favLang = input()
# Print str conditional statement based on user input
if favLang == (engLang):
    print ('Hello my friend!')
elif favLang == (spnLang):
    print('Hola Amigo!')
elif favLang == (frLang):
    print('Bonjour, mon ami!')
else:
    print ('That is not one of the languages I mentioned')
# make sure that your code contains comments explaining your logic!

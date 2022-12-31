from termcolor import colored as c
from os import name, system
#from time import sleep


def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')

def title_style(title):
    clear()
    print(c('=' * 25, 'yellow'))
    print(c(title, 'magenta'))
    print(c('=' * 25 + "\n", 'yellow'))


def options(number, actions):
	for i in range(0, len(number)):
		print(c(f"[{number[i]}] ", 'magenta') + c(f"{actions[i]}", 'yellow'))


def menu_internal():
	numbers = ['1', '2']
	actions = ['ɴᴏᴠᴀ ᴏᴘᴇʀᴀᴄᴀᴏ', 'sᴀɪʀ']
	options(numbers, actions)
	match input(c( '\n\nᴅɪɢɪᴛᴇ ᴀǫᴜɪ: ', 'blue' )):
		case '1':
			menu_operations()
		case '2':
			clear()
			system('exit')

def menu_operations():
	title_style('        ᴏᴘᴇʀᴀᴄᴏᴇs')
	numbers = [ '1', '2', '3', '4', '5']
	actions = [ 'ᴀᴅɪᴄᴀᴏ', 'sᴜʙᴛʀᴀᴄᴀᴏ', 'ᴍᴜʟᴛɪᴘʟɪᴄᴀᴄᴀᴏ', 'ᴅɪᴠɪsᴀᴏ' , 'ᴠᴏʟᴛᴀʀ' ]
	options(numbers, actions)
	operations()


def operations():
    type = input(c( '\n\nᴅɪɢɪᴛᴇ ᴀǫᴜɪ: ', 'blue' ))
    if type == '5':
    	menu_main()
    title_style('        ᴏᴘᴇʀᴀᴄᴏᴇs')
    n1 = int(input(c('1° valor: ', 'yellow')))
    n2 = int(input(c('2° valor: ', 'yellow')))
    match type:
        case '1':
            a = n1 + n2
            b = '+'
        case '2':
            a = n1 - n2
            b = '-'
        case '3':
            a = n1 * n2
            b = '*'
        case '4':
            a = n1 / n2
            b = '/'
        case _:
            clear()
            print('ᴏᴘᴄᴀᴏ ɪɴᴠᴀʟɪᴅᴀ')
            sleep(0.55)
            operations()
    title_style('        ᴏᴘᴇʀᴀᴄᴏᴇs')
    print(f"{n1} {b} {n2} = {a}\n")
    menu_internal()
    


def menu_main():
    title_style('          ᴍᴇɴᴜ')
    numbers = [ '1', '2' ]
    actions = [ 'ᴏᴘᴇʀᴀᴄᴏᴇs', 'sᴀɪʀ' ]
    options(numbers, actions)
    text = c( '\n\nᴅɪɢɪᴛᴇ ᴀǫᴜɪ: ', 'blue' )
    match input(text):
        case '1':
            menu_operations()
        case '2':
            clear()
            system('exit')
    





# started
menu_main()



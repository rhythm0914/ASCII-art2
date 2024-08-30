from pyfiglet import Figlet

blue = '\033[34m'
reset = '\033[0m'

figlet = Figlet(font='small')

text = "RYAN JOSEPH"

ascii_art = figlet.renderText(text)

print(f"{blue}{ascii_art}{reset}")

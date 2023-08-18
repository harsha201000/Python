import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print("Colored Console Output : ")

print("------------------------------------")

print(f"{Fore.WHITE}{Back.BLACK}{Style.NORMAL}Terminal >_:)")

print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}Hello World")
print(f"{Fore.BLUE}{Back.YELLOW}{Style.BRIGHT}Python 3.11.4 64-bit")


# Changes text color
print(Fore.GREEN + "Harsha")
# Changes background color
print(Back.CYAN + "Harsha")

# CHanges Text Color and bg color
print(f"{Fore.GREEN}{Back.WHITE}" + "Harsha")

# print color text in rainbow color
print(f"{Fore.RED}H{Fore.YELLOW}A{Fore.GREEN}R{Fore.LIGHTBLUE_EX}S{Fore.CYAN}H{Fore.MAGENTA}A")
print(f"{Fore.LIGHTGREEN_EX}M{Fore.LIGHTCYAN_EX}A{Fore.LIGHTBLUE_EX}L{Fore.LIGHTRED_EX}I{Fore.LIGHTGREEN_EX}P{Fore.LIGHTBLUE_EX}E{Fore.RED}D{Fore.RED}D{Fore.LIGHTBLUE_EX}I")

# print background text in different colors
print(f"{Back.LIGHTGREEN_EX}H{Back.YELLOW}A{Back.RED}R{Back.BLUE}S{Back.CYAN}H{Back.MAGENTA}A")
print(f"{Back.LIGHTGREEN_EX}M{Back.YELLOW}A{Back.RED}L{Back.BLUE}I{Back.CYAN}P{Back.MAGENTA}E{Back.LIGHTRED_EX}D{Back.LIGHTRED_EX}D{Back.LIGHTCYAN_EX}I")

# print fg text, bg text and style
print(f"{Fore.GREEN}{Back.BLUE}{Style.BRIGHT}" + "Harsha")

print("------------------------------------")
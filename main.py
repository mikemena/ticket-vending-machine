from colored import Fore, Back, Style

color: str = f"{Style.BOLD}{Fore.WHITE}{Back.BLUE}"
print(f"{color}Background color blue with bold white text!{Style.reset}")

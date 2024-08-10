import colorama 
from colorama import Fore 
colorama.init(autoreset=True)

# Define color constants for terminal output
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RESET = Fore.RESET

def main():
    # Input from user for the text file and handle file errors
    while True:
        txt_file = input(CYAN+"Enter the text file: "+RESET)
        
        try:
            with open(txt_file, 'r') as file:
                words = file.read().split()  # Read words from the file
            break
        
        except FileNotFoundError:
            print(RED+"Error! File not found")
        except IOError:
            print(RED+"Error! File not read")
    
    # input from user for the length of words to filter
    while True:
        try:
            lenght = int(input(CYAN+"Enter the length of word: "+RESET))
            if lenght <= 0:
                print(RED+"Enter size greater than 0")
            else:
                break
            
        except ValueError:
            print(RED+"Please enter size as an integer.")

    # Input from user for the type of filtering to apply
    while True:
        try:
            choice = int(input("\n1"+CYAN+" for filter only number of characters\n"
                        +RESET+"2"+CYAN+" for position character finding\n"
                        +RESET+"3"+CYAN+" for random character finding\n"
                        +RESET+"4"+CYAN+" for both\nEnter: "+RESET))
            break
        
        except ValueError:
            print(RED+"Please enter only numbers.")
    
    # Initialize lists to hold user-defined filters
    ram_charcter = [] 
    position = []
    charcter = []    
    size = 0 
    
    # Filter based on chosen criteria
    if choice == 1:
        print(YELLOW+"\nResult words with length:")
        
    elif choice == 2:
        try:
            size = int(input(CYAN+"Enter the number of index characters you want to enter: "+RESET))
        except ValueError:
            print(RED+"Error! Enter only numbers")
        
        # Get position-based characters from the user
        for i in range(size):
            print()
            while True:
                p = int(input(f"{CYAN}Enter the index based({i+1}) position of character: {RESET}"))
                if p >= 1 and p <= lenght:
                    c = input(CYAN+"Enter the character at index based position: "+RESET)
                    break
                else:
                    print(RED+"Error! Please enter the index under size.")
            position.append(p)
            charcter.append(c)  
        print(YELLOW+"\nResult words with position indexing:")
    
    elif choice == 3:
        try:
            size = int(input(CYAN+"Enter the size of random characters you want to enter: "+RESET))
        except ValueError:
            print(RED+"Error! Enter only numbers.")
        print()
        
        # Get random characters from the user
        for i in range(size):
            c = input(f"{CYAN}Enter the {i+1} character at random position: {RESET}")
            ram_charcter.append(c)
        print(YELLOW+"\nResult words with random position indexing:")
    
    elif choice == 4:
        try:
            size = int(input(CYAN+"How many position index characters you want to enter: "+RESET))
        except ValueError:
            print(RED+"Error! Enter only numbers.")
        
        # Get both position-based and random characters from the user
        for i in range(size):
            print()
            while True:
                p = int(input(f"{CYAN}Enter the index based({i+1}) position of character: {RESET}"))
                if p >= 1 and p <= lenght:
                    c = input(CYAN+"Enter the character at index based position: "+RESET)
                    break
                else:
                    print(RED+"Error! Please enter the index under size.")
            position.append(p)
            charcter.append(c)  
        
        try:
            size2 = int(input(CYAN+"Enter the size of random characters you want to enter: "+RESET))
        except ValueError:
            print(RED+"Error! Enter only numbers.")
        print()
        
        for i in range(size2):
            c = input(f"{CYAN}Enter the {i+1} character at random position: {RESET}")
            ram_charcter.append(c)
            
        print(YELLOW+"\nResult words with position and random indexing:")
    
    # Filter words based on user-defined criteria
    output = filtered(words, lenght, position, charcter, ram_charcter)
    
    # Print the filtered words
    for i in output:
        print(GREEN+i+"     ", end='')
    
    # Optionally save the results to a file
    ch = input(CYAN+"\n\nDo you want to save the result to a text file (y/n): "+RESET)
    if ch == 'y':
        name = input(CYAN+"Please enter the file name: "+RESET)
        with open(name, 'w') as file:
            for i in output:
                file.write(i+"     ")
        print(YELLOW+"File saved successfully.")

def filtered(words, lenght, position=0, charcter=None, ram_charcter=None):
    
    # Clean and filter words based on length
    clean_words = [word.replace('.','').replace(',','').replace(':','') for word in words]
    
    # Filtering word according to given lenght
    filtered_words = [word for word in clean_words if len(word) == lenght]
    
    # Further filter words based on position-based characters
    if position and charcter:
        filtered_words = [
            word for word in filtered_words
            if all(
                len(word) >= pos and word[pos - 1] == char
                for pos, char in zip(position, charcter)
            )
        ]
    
    # Further filter words based on random characters
    if ram_charcter:
        filtered_words = [word for word in filtered_words
                          if all(char in word for char in ram_charcter)
        ]
    
    # Convert to lowercase and remove duplicates
    lower_case = [word.lower() for word in filtered_words]
    unique_words = list(set(lower_case))
    return unique_words    

if __name__ == "__main__":
    main()

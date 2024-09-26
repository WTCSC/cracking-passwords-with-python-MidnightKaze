import argparse
import hashlib

"""Sets up a hashing fuction that uses multiple differnt algorithms"""
def hashtfs_word(word):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(word.encode())
    return sha256_hash.hexdigest()

def hash512_word(word):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(word.encode())
    return sha512_hash.hexdigest()

def hashmd5_word(word):
    md5_hash = hashlib.md5()
    md5_hash.update(word.encode())
    return md5_hash.hexdigest()

"""Begins by setting up the parsing using ArgParse"""
def main():
    parser = argparse.ArgumentParser(description= 'Takes a word list and uses it to crack the password')
    parser.add_argument('password_file', help= 'File with the passwords to crack')
    parser.add_argument('word_file', help= 'The word list (or file) used to crack the password')
    parser.add_argument('-a', '--algorithm', choices=['sha256','sha512','md5'], default= 'sha256', help= 'Allows the user to choose specific algorithm')
    args = parser.parse_args()

    """Opens each respective file using a 'With' statment for optimization ('With' statements will automatically close making the code more efficient)"""
    with open(args.password_file, 'r') as passwords, open(args.word_file, 'r') as words: 
        user_passwords = passwords.readlines() #passes the contents of the password file into a list with readlines
        word_list = words.readlines() #does the same as passwords but with the word list file

    """Initiates two lists for use in the for loop following"""
    hashed_passwords = [] 
    usernames = [] 

    """Splits each username and password combo with a split at the ':' and appends them to their respective list"""
    for combo in user_passwords:
        username, password = combo.strip().split(':') #uses strip to remove any possible new line characters that may later impact the code
        usernames.append(username)
        hashed_passwords.append(password)

    """Uses the hashing function from before to hash the word list and add it to a list"""
    if args.algorithm == 'sha256':
        hashed_wordlist = [hashtfs_word(word.strip()) for word in word_list] #uses strip to remove any possible new line characters that may later impact the code
    
    if args.algorithm == 'sha512':
        hashed_wordlist = [hash512_word(word.strip()) for word in word_list]

    if args.algorithm == 'md5':
        hashed_wordlist = [hashmd5_word(word.strip()) for word in word_list]

    """Uses enumerate to compare the passwords to the hashed words in the hashed word list"""
    for p, hashed_password in enumerate(hashed_passwords): #enumerate is a good choice as it can store the index along with the word which...
        for w, hashed_word in enumerate(hashed_wordlist):
            if hashed_password == hashed_word:
                print(f"{usernames[p]}:{word_list[w].strip()}") #...we can call for the final print statement :D
                break #ensures the for loop breaks before starting the next username and password combo checking

"""Closes out the parsing"""
if __name__ == '__main__':
    main()
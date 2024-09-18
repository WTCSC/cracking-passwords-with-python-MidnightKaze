import argparse
import hashlib

def main():
    parser = argparse.ArgumentParser(description= 'Takes a word list and uses it to crack the password')
    parser.add_argument('password_file', help= 'File with the passwords to crack')
    parser.add_argument('word_file', help= 'The word list (or file) used to crack the password')
    args = parser.parse_args

    passwords = open(args.password_file, 'r') #opens the password file passed through in read mode
    words = open(args.word_file, 'r') #opens the word list passed through in read mode

    #need to extract just the password using a split

    user_password = passwords.readlines() #splits the user+password combos into lines
    word_list = words.readlines() #splits the word list into lines

    password = ((user_password.split(':')[1]) for p in user_password) #splits the user+password combos at the ':' so you get just the password (index 1)

    """for word in word_list:
         hashed_wordlist = []
         hashed_wordlist.append(hashtfs_word(word.strip()))

    print(hashed_wordlist)"""

    passwords.close()
    words.close()

""""""

def hashtfs_word(word): #hashes the words from word list

    sha256_hash = hashlib.sha256()

    sha256_hash.update(word.encode())

    return sha256_hash.hexdigest()

""""""

if __name__ == '__main__':
        main()
import argparse
import hashlib

def hashtfs_word(word):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(word.encode())
    return sha256_hash.hexdigest()

def main():
    parser = argparse.ArgumentParser(description= 'Takes a word list and uses it to crack the password')
    parser.add_argument('password_file', help= 'File with the passwords to crack')
    parser.add_argument('word_file', help= 'The word list (or file) used to crack the password')
    args = parser.parse_args()

    with open(args.password_file, 'r') as passwords, open(args.word_file, 'r') as words: 
        user_passwords = passwords.readlines() 
        word_list = words.readlines()

    hashed_passwords = [] 
    usernames = [] 

    for combo in user_passwords:
        username, password = combo.strip().split(':')
        usernames.append(username)
        hashed_passwords.append(password)

    hashed_wordlist = [hashtfs_word(word.strip()) for word in word_list]

    for p, hashed_password in enumerate(hashed_passwords):
        for w, hashed_word in enumerate(hashed_wordlist):
            if hashed_password == hashed_word:
                print(f"{usernames[p]}:{word_list[w].strip()}")
                break

if __name__ == '__main__':
    main()
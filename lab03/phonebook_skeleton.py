#!/usr/bin/env python

import sys
import os
import stat

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        with open('./python_phonebook_entries', 'a') as f:
            #print(len(sys.argv))
            constent = sys.argv[2]
            i = 3
            while (i < len(sys.argv)):
                constent = constent + " " +sys.argv[i]
                i += 1
            constent += "\n"
            #print(constent)
            f.write(constent)
        #os.chmod(PHONEBOOK_ENTRIES, stat.S_IRWXU)
        return
        # YOUR CODE HERE #

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            with open('./python_phonebook_entries', 'r') as f:
                for line in f:
                    print(line,  end = '')
            return


            # YOUR CODE HERE #

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        #print(name)
        with open('./python_phonebook_entries', 'r+') as f:
            for line in f:
                if (name in line):
                    line = ""
        return



        # YOUR CODE HERE #

    elif sys.argv[1] == "clear":
        with open('./python_phonebook_entries', 'w') as f:
            f.seek(0,0)
            f.truncate()
            return
        # YOUR CODE HERE #

    else:
        name = " ".join(sys.argv[1:(len(sys.argv)-1)])
        with open(PHONEBOOK_ENTRIES, 'r+') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            print(lookup, end = '')
            return
            # YOUR CODE HERE #


if __name__ == "__main__":
    main()

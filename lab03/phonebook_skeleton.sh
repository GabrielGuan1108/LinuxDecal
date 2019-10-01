#!/bin/bash

PHONEBOOK_ENTRIES="bash_phonebook_entries"


if [ "$#" -lt 1 ]; then
    exit 1

elif [ "$1" = "new" ]; then
  if [ ! -d $PHONEBOOK_ENTRIES ]; then
    touch $PHONEBOOK_ENTRIES
    chmod 777 $PHONEBOOK_ENTRIES
  fi


  Name="$2 $3 $4"
  #echo $Name
  echo $Name >> $PHONEBOOK_ENTRIES
    # YOUR CODE HERE #

elif [ "$1" = "list" ]; then
    if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
        echo "phonebook is empty"
    else
      cat $PHONEBOOK_ENTRIES
        # YOUR CODE HERE #
    fi

elif [ "$1" = "remove" ]; then
    sed '/'$2'/d' $PHONEBOOK_ENTRIES
    # YOUR CODE HERE #

elif [ "$1" = "clear" ]; then
    # YOUR CODE HERE #
    echo "" > $PHONEBOOK_ENTRIES

else
    grep $2 $PHONEBOOK_ENTRIES
     # YOUR CODE HERE #
fi

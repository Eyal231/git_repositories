#!/bin/bash

ulib=$HOME/work/git_repositories/bash/users
pwb="$(pwd)/users"



while true 
        do
                echo -n "user> " 
                read command
                case $command in
                        new)
                               echo -n  "enter new user name: "
                               read username

                                     if [ ! -f $pwb/"${username}.user" ]; then
                                             echo "user: $username " > $pwb/"${username}.user"
                                             echo "password: $[ $RANDOM % 40000 + 10000 ] " >> $pwb/"${username}.user"
                                             echo user '"'$username'"' created and file in "$pwb"
                                     else
                                             echo "name allredy exsist"
                                     fi
                                     ;;
                         exit)
                               echo exit=1
			       ;;

                        esac
		done


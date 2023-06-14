#!/bin/bash
#

pwb="$(pwd)/users"
SCRIPT_PATH="$(pwd)/while.sh"

## check if the user directory is exist:
if [ ! -d $pwb ]; then 

	echo "directory 'users' is'nt exist"
    echo "do you need help for make the directory? type 'yes' or leav empty"
    read answer

  ##if the directori is not exist, script can help or leave.
  	   if [ $answer = yes ]; then
           mkdir $pwb
           echo "directory biuld up" 
	       "$SCRIPT_PATH"
					     
     elif [ $answer != yes ]; then
	       ##if the directori is not exist, and the user dosen't need help.
	       echo "directory 'users' is'nt exist"
	       echo  "come back when you will have it"
	   fi
   elif [ -d $pwb ]; then 
	   "$SCRIPT_PATH"
fi 

	  

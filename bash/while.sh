#!/bin/bash
#!/work/git_repositories/bash/

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
		list)
			list=$(find "$pwb" -name "*.user" -type f -printf "%f\n" | sort)
			for file in $list; do
				filename=$(basename "$file" .user)
				echo "$filename"
			done

   # if [ -f ${#file[@]} -eq 0 ]; then
      #  echo "No users"
   # else
      ##  output_file="user_list.txt"  # Name of the output file
      ## rm -f "$output_file"  # Remove the file if it already exists

     #   for file in "${files[@]}"; do
       #     username=$(sed -n 's/^name: \(.*\)/\1/p' "$file")
          #  echo "$username" <> "$output_file"
       # done

       # if [ -s "$output_file" ]; then
       #     cat "$output_file"  # Print the contents of the output file
       # else
       #     echo "No users"
       # fi

       # rm -f "$output_file"  # Remove the output file
   # fi
   
				     ;;
			     del)
				     echo -n "enter user to delete : "
				     read del_name

				     if [ -f "$pwb/"${del_name}.user"" ]; then
					     rm "$pwb/"${del_name}.user""
					     echo "$del_name was delited"
				     else 
					     echo "$del_name dosen't exeist in the list. "
				     fi
				     ;;
			     show)
				     echo -n "enter name to chack ditailes : "
				     read chack_name

				     if [ -f "$pwb/"${chack_name}.user"" ]; then
					     cat "$pwb/"${chack_name}.user""
				     else
					     echo "user $chack_name is not in the list"
				     fi
				     ;;
                         exit)
                                 if [ $command = exit ]; then
					 echo "thenk you for your time"
					 break;
                              fi
			       ;;

                        esac
		done


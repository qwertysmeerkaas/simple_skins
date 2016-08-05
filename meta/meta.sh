for skin in *.png do;
  if [ -e ../meta/$skin.txt ] 
  then
    printf "I already have $skin - skipping\n"
  else
    printf "New skin $skin - generate meta-entry\n"
    printf "Name = \"$skin\\nAuthor = \"Minetestskins\"" > ../meta/$file.txt

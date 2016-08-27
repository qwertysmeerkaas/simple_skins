for skinname in *.png; 
do
  filename=$(basename "$skinname")
  skin="${filename%.*}"
  if [ -e ../meta/$skin.txt ] 
  then
    printf "I already have $skin - skipping\n"
  else
    printf "New skin $skin - generate meta-entry at ../meta/$skin.txt \n"
    printf "Name = \"$skin\",\nAuthor = \"Minetestskins\",\nDescription = \"\",\nComment = \"\"," > ../meta/$skin.txt
  fi
done

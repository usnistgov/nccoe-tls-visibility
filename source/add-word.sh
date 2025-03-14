# ./add-word word1 word2 word3

for word in "$@"; do
  echo "$word" >> dictionary.txt
done


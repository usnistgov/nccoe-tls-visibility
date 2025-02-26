#!/bin/bash
# ./spell-check.sh


RST_FOLDERS=("AppCScenarios" "AppendixBGeneration" ".")

for folder in ${RST_FOLDERS[@]}; do
  for m in $folder/*.rst; do
    echo "========= UNKNOWN WORDS FOUND IN $m ========"
    cat $m | aspell -p ./dictionary.txt list | sort -u
  done
done

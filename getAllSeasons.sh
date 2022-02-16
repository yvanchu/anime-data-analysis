#!/bin/bash
declare -a seasons=("Winter" "Spring" "Summer" "Fall")
for year in {2001..2021}
do 
    for season in "${seasons[@]}"
    do
        python3 getAnimeBySeason.py "$year" "$season" > "data/${year}${season}.csv"
    done
done

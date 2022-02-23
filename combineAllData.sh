#!/bin/bash
declare -a seasons=("Winter" "Spring" "Summer" "Fall")
for year in {2001..2021}
do 
    for season in "${seasons[@]}"
    do
        tail -n +2 "data/${year}${season}.csv" >> "data/allData.csv"
        # python3 getAnimeBySeason.py "$year" "$season" > "data/${year}${season}.csv"
    done
done

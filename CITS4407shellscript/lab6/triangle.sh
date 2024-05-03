#!/bin/bash

if [ $# -gt 1 ] && [ $1 = "-r" ]; then
    size=$2
else
    size=4
fi

row=1
while [[ $row -le $size ]]
do
    col=1
    while [[ $col -le $row ]]
    do
        if [[ $col -eq $row ]]; then
            echo -n "\\"
        elif [[ $col -eq 1 ]]; then
            echo -n "|"
        elif [[ $((row%2)) -eq 1 ]]; then
            echo -n "L"
        else
            echo -n "*"
        fi
        col=$(($col+1))
    done
    row=$(($row+1))
    echo
done



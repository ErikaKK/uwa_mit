#!/bin/bash


# if [ $# -ne 1 ]; then 
#     echo "Usage: $0 <directory>"
#     exit 1
# fi
dir='.'

while [ $# -gt 0 ]; do
    # case $1 in 
    # -h)     
    #     echo "-d DIRECTORY Count files in DIRECTORY instead of ."
    #     echo
    #     echo "-h Display this help message and exit"
    #     exit 0;;
    # -d) 
    #     if [ -z $2 ]; then
    #         echo "Missing argument for -d"
    #         exit 1
    #     fi
    #     dir=$2
    #     shift
    #     ;;
    # esac
    # shift
    if [ $1 = '-help' -o $1 = '-h' ]; then
        echo "-d DIRECTORY Count files in DIRECTORY instead of ."
        echo
        echo "-h Display this help message and exit"
        exit 0
    elif [ $1 = '-d' ]; then
        if [ -z $2 ]; then
            echo "Missing argument for -d"
            exit 1
        fi
        dir=$2
        shift
    else
        dir=$1
    fi
    shift
done

if [ ! -d $dir ]; then
    echo "Error: '$dir' is not a directory or does not exist."
    exit 1
fi

largest=0
sum=0

for file in $dir/*; do
    if [ -f "$file" ];then
        size=$(wc -c < "$file" | tr -d '[:space:]')
        filename=$(basename $file)
        echo "$size $filename"
        if [ $largest -lt $size ];then
            largest=$size
            largest_file=$filename   
        fi      
        sum=$(($sum+$size))
    fi    
done

#largest=$(echo "$largest" | tr -d '[:space:]')
#largert_file=$(echo "$largest_file" | tr -d '[:space:]')

echo "Largest is $largest in $largest_file" 
echo "Sum is $sum"
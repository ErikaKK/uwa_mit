#!/bin/bash

while [[ $# -gt 0 ]]
do 
    echo $2 > $1
    shift
    shift
done

#!/bin/bash
BINARY=2
T=1
number=$RANDOM

if [ $# -eq 0 ]
  then
    echo "Syntax: $0 led1 led2"
    gpio readall
    exit
fi

if [ -z "$2" ]
  then
    echo "LED 2 not specified"
    exit
fi

led1=$1
led2=$2

gpio -g mode $led1 out
gpio -g mode $led2 out

let "number %= $BINARY"
#  Note that    let "number >>= 14"    gives a better random distribution
#+ (right shifts out everything except last binary digit).
if [ "$number" -eq $T ]
then
  echo "Lighting LED 1: $led1"
  gpio -g write $led1 1
  gpio -g write $led2 0
else
  echo "Lighting LED 2: $led2"
  gpio -g write $led1 0
  gpio -g write $led2 1
fi  

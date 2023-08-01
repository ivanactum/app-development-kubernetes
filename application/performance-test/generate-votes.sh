#!/bin/sh

# create 3000 votes (2000 for option a, 1000 for option b)
ab -n 1000 -s 120 -t 999 -k -c 500 -p posta -T "application/x-www-form-urlencoded" http://vote.omai.ltd/
ab -n 1000 -s 120 -t 999 -k -c 500 -p postb -T "application/x-www-form-urlencoded" http://vote.omai.ltd/
ab -n 1000 -s 120 -t 999 -k -c 500 -p posta -T "application/x-www-form-urlencoded" http://vote.omai.ltd/

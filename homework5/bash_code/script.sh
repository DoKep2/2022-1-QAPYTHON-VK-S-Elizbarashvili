#!/bin/bash
echo "----------Requests amount:----------" > result.txt
wc -l < access.log >> result.txt
echo "----------Requests amount by type (amount, type):----------" >> result.txt
awk '{print $6}' access.log | cut -c 2- | sort | uniq -c | sort -rn >> result.txt
echo "----------10 the most frequent requests (amount, url):----------" >> result.txt
awk '{print $7}' access.log | sort | uniq -c | sort -rn | head -n 10 >> result.txt
echo "----------5 the biggest requests with request status 4XX (url, status code, size, ip):----------" >> result.txt
awk '{print $7, $9, $10, $1}' access.log | grep -E ' 4.. ' | sort -rnk3 | head -n 5 >> result.txt
echo "----------Top-5 users by amount of requests with status 5XX (amount, ip):----------" >> result.txt
awk '{print $1, $9}' access.log | grep -E ' 5..$' | sort | uniq -c | sort -rn | head -n 5 | awk '{print $1, $2}' >> result.txt



#!/bin/bash

123.123.23.3
123.123.23.2
123.123.23.4
123.123.23.5
123.123.23.3
123.123.23.6
123.123.23.3
123.123.23.3
123.123.23.6

a=10
b=20
# 新建文件、目录
# mkdir test02
# cd test02
# echo "hello">test03.txt
# cat test03.txt

# 基本运算
echo `expr $a + $b`
echo `expr $a \* $b`
echo `expr $a % $b`

# 脚本参数传递
echo $1,$2,$3
echo "文件名" $0
echo "参数数量" $#
echo "all" $*
echo "return" $?
echo "hello"

# 控制语句
if [[ $a > $b ]]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi

# for循环
for str in This is a string
do
    echo $str
done

# while循环
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
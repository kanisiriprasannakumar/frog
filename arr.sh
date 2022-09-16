echo "enteer any number that is must be between zero to six and then press enter after enterd the number"
read num
arr=( sunday monday tuesday wednesday thursday friday saturday )
if [ $num == 0 ]
then

echo "${arr[0]}"
elif [ $num == 1 ]
then
        echo "${arr[1]}"
elif [ $num == 2 ]
then
echo "${arr[2]}"
elif [ $num == 3 ]
then
        echo "${arr[3]}"
elif [ $num == 4 ]
then
echo "${arr[4]}"
elif [ $num == 5 ]
then
        echo "${arr[5]}"
elif [ $num == 6 ]
then
echo "${arr[6]}"
else
        echo "i dont know wish week day this "
echo "i said only the numbers from zero to six only"

fi


while true; 
do 
echo Script Run Time: `date +"%Y-%m-%d %T"`
result=`python ./bestbuy.py`; 
echo $result
sleep 90; 
done
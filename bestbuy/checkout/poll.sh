while true; 
do 
echo Script Run Time: `date +"%Y-%m-%d %T"`
result=`python3.9 ./bestbuy-checkout.py`; 
echo $result
sleep 90; 
done
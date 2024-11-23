if [ "$EUID" -ne 0 ]
then echo "Please run as root"
exit
fi

apt install python
pip install -r requirements.txt

## Save crontab to new file
#crontab -l > newcron
#
## Write to new file
#echo "@reboot" >> newcron
#
## Save file to crontab
#crontab newcron
#rm newcron
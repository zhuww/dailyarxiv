cd /homes/zhuww/work/shell/lynxget
. ./updat_archive
sed -f delete new > new.txt
sed -f programs new.txt > news.txt
#for name in zhuww xubx qianl
for name in zhuww 
do
gawk -f PATTERN.$name news.txt > mailbody.$name
#cat header.$name > newsmail.$name
#cat mailbody.$name >> newsmail.$name
cat mailbody.$name >> database.$name
#send ./newsmail.$name 
#cat mailbody.$name | mail zhuww -s "New issues on archive `date +%D`"
python body2html.py
python sendmail.py
done

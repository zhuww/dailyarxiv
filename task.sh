cd /homes/zhuww/work/shell/lynxget
sleep 30
#. ./update_archive http://arxiv.org/list/astro-ph/new
python lynx.py http://arxiv.org/list/astro-ph/new
cat new > todaynews
sleep 30
#. ./update_archive http://arxiv.org/list/gr-qc/new
python lynx.py http://arxiv.org/list/gr-qc/new
cat new >> todaynews
sed -f delete todaynews > new.txt
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
rm -f new todaynews new.txt news.txt

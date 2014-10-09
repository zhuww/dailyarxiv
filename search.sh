workpath=/homes/janeway/zhuww/work/shell/lynxget
currpath=`pwd`
#. ./updat_archive
#sed -f delete new > new.txt
#sed -f programs new.txt > news.txt
#for name in zhuww xubx qianl
for name in zhuww 
do
cd $workpath
sed -f programs database.$name > searchdb.$name
#gawk -f PATTERN.$name searchdb.$name > .$name
sed -e "s/pattern/$*/g" search.PATTERN > sechpatt.zhuww
gawk -f sechpatt.zhuww searchdb.$name > searchresult.$name
cd $currpath
cat $workpath/searchresult.$name | more
#cat header.$name > newsmail.$name
#cat mailbody.$name >> newsmail.$name
#cat mailbody.$name >> database.$name
#send ./newsmail.$name 
#cat mailbody.$name | mail zhuww -s "New issues on archive `date +%D`"
done

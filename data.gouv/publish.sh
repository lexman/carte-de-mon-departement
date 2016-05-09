export API="https://www.data.gouv.fr/api/1/"
export XAPIKEY="eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiNTRiYWViNGJjNzUxZGY2MmI1NWZhNWEyIiwidGltZSI6MTQ2MjczNDQ0MC43OTk5MzF9.SewugL3zJH99qGO9Ta5g17oZ_-fMiwf5ZxhvT7nUojU"

DEPTS_CONT=`cat ../departement_metropolitain.txt|tr '\r\n' '  '`
DEPTS_LOIN="2A 2B 971 972 973 974 976"

#http POST $API'datasets/carte-des-departements-2/resources/' X-API-KEY:$XAPIKEY title="departement-$NUM" filesize=$FILESIZE format="shapefile" mime="application/zip" url="http://sisyphus.lexman.org/workflows/carte_de_mon_departement/workspace/publish/departement-$NUM.zip" 

for NUM in $DEPTS_CONT $DEPTS_LOIN
do
    echo $NUM
    #$FILESIZE=`du ../zips/departement-$NUM.zip | awk '{print $1}'`
    http POST $API'datasets/carte-des-departements-2/resources/' X-API-KEY:$XAPIKEY title="departement-$NUM" format="shapefile" mime="application/zip" url="http://sisyphus.lexman.org/workflows/carte_de_mon_departement/workspace/publish/departement-$NUM.zip" 
done

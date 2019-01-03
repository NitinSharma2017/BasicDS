import cx_Oracle
import csv


#declare below your sql statement


SQL1='''
          select  X from (

) order by ss

     '''
SQL2='''
          select  X from (
) order by ss

     '''

SQL3='''
          select  X from (

     '''

SQL4='''
          select  X from (
) order by ss

     '''



#provide the oracle login details in connection object  
connection = cx_Oracle.connect('schema/pwd')
 
cursor = connection.cursor()


#declare below the location/name of output file 
filename="D:\CVM.TXT"
FILE=open(filename,"w");


cursor.execute(SQL1)

for row in cursor:
    FILE.write("".join(row))
    FILE.write('\n')
FILE.close()


#declare below the location/name of output file 
filename="D:\CVM.TXT"
FILE=open(filename,"w");


cursor.execute(SQL2)

for row in cursor:
    FILE.write("".join(row))
    FILE.write('\n')
FILE.close()


#declare below the location/name of output file 
filename="D:\CVM.TXT"
FILE=open(filename,"w");


cursor.execute(SQL3)

for row in cursor:
    FILE.write("".join(row))
    FILE.write('\n')
FILE.close()

#declare below the location/name of output file 
filename="D:\CVM.TXT"
FILE=open(filename,"w");


cursor.execute(SQL4)

for row in cursor:
    FILE.write("".join(row))
    FILE.write('\n')
FILE.close()


cursor.close()
connection.close()



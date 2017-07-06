import ics
import calendar
c_c = ics.Calendar()

#Input will be courses same as course name in the table
courses=["BIO314(203)"]
import pandas
df=pandas.read_excel("065634_Schedule_sem7.xlsx") #Add the modified file name
df=df.set_index("DAY")
def check(x):
    return str(x).split('\n')

df=df.applymap(check)

master=[] #(course,day,time)

for c in courses:
    #c="CHM311(201)"
    def course(x):
        global c
        if c in x:
            return True
        else:
            return False
    cf=df.applymap(course)
    for i in cf.index:
        for j in df.columns:
            if cf[j][i] == True:
                master.append((c,i,j))

    
print cf
#"20170801"to"20170919"-"20171004"to"20171121"
#--------------Creating working days---------------------
from datetime import date,timedelta
d=[]
d1 = date(2017,8,1)
d2 = date(2017,9,19)

delta= d2-d1
for i in range(delta.days + 1):
    d.append(d1 + timedelta(days=i))

d1 = date(2017,10,4)
d2 = date(2017,11,21)

delta= d2-d1
for i in range(delta.days + 1):
    d.append(d1 + timedelta(days=i))
    
'''    
#------------Converting them to day names------------------------
days=[]
for i in d:
    days.append(calendar.day_name[i.weekday()])
#-----------Converting to Date format of ICS------------------
ddates=[]
for i in d:
    ddates.append(i.strftime("%Y%m%d"))
#--------------------------------------------------------------

#date=YYYYMMDD done
#time=HH:MM:SS

#Need to get stime and end time
stime={"08:00:00"}
etime={"08:30:00"}
'''


for x in d:
    for y in master:
        if calendar.day_name[x.weekday()].lower() == y[1].encode('utf8').lower():
            e = ics.Event()
            course_name=y[0]
            [start_time,end_time]=y[2].encode('utf-8').split('-')
            e.name = course_name
            d_x=x.strftime("%Y,%m,%d").split(',')
            st_x=start_time.split(':')
            et_x=end_time.split(':')
            b_a= map(int,(d_x + st_x))
            e_a= map(int,(d_x + et_x))
            print b_a
            e.begin = tuple(b_a)
            e.end = tuple(e_a)
            #e.location =str(location)
            c_c.events.append(e)


print c_c.events

with open('timetable.ics', 'w') as f:
    f.writelines(c_c)

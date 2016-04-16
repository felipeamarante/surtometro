from flask import Flask, redirect, render_template
import datetime, time
app = Flask(__name__)

#global fistDay, today, recordDay, counterDays


firstDay = datetime.datetime.now()
today = datetime.datetime.now()
recordDay = datetime.datetime.now()
counterDays = today - firstDay
jinjaDay = datetime.datetime.now()
jinjaRecord = datetime.datetime.now()


print today
print firstDay


@app.route("/")
def core():
    global today, recordDay, counterDays, today, jinjaDay, jinjaRecord
    today = datetime.datetime.now()
    counterDays = today - firstDay

    print "JinjaDay is %s " % jinjaDay
    print "JinjaRecord is %s " % jinjaRecord



    if firstDay < today:
        counterDays = today - firstDay
        print counterDays
        jinjaDay = counterDays.seconds

#TODO
#    if recordDay - today <= counterDays:
#        recordDay = counterDays
#        print recordDay
#        jinjaRecord = recordDay.seconds


    return render_template('index.html', jinjaDay=jinjaDay, jinjaRecord=jinjaRecord)



@app.route("/reset")
def resetCounter():
    global firstDay
    firstDay = datetime.datetime.now()
    return redirect("")





if __name__ == "__main__":
    app.run(debug=True)



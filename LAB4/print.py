from flask import Flask
app = Flask(__name__)
import restaurant as restaurant_system
import numpy as np


@app.route('/')
def index():
    global myRestraunt
    table = myRestraunt.get_table()
    result ="<html><h1>Restaurant Booking Table</h1><table>"
    shale_t = table.shape
    for day in range(0,shale_t[0]):
        result+= "<tr>\n"
        result+="\t<th>\n DAY : "+str(day+1)+"\t</th>\n"
        for time in range(0,24):
            result += "\t<th>"+str(time)+"</th>\n"
        result+= "</tr>\n"
        for t in range(0,shale_t[1]):
            result+= "<tr><td> TABLE :\n"+ str(t) + "</td>\n"
            for time in range(0, shale_t[2]):
                result += "<td>" + str(int(table[day,t,time]))+ "</td>"
            result+= "</tr>"
    result += "</table></html>"
    return result
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == "__main__":
    db = restaurant_system.database_connection("127.0.0.1", "root", "root", "restaurant_system")
    db.connect()
    myRestraunt = restaurant_system.restraunt()
    
    print "\n\n *** LOGIN FORM ***\n"
    uname = raw_input("USERNAME:  ")

    passw = raw_input("\n PASSOWRD:  ")
    
    if db.authenticate(uname, passw):
        print "\n ***** AUTHENTICATED *****\n"
        myRestraunt.set_tables(1, 3, 8, 4)
        myRestraunt.book_table(12, 0, 12, 6,"Kumail",db=db)
        myRestraunt.book_table(12, 0, 6, 4,"Noor",db=db)
        myRestraunt.book_table(12, 0, 4, 4,"Hassan",db=db)
        myRestraunt.book_table(12, 0, 2, 4,"Aminah",db=db)
        myRestraunt.book_table(12, 1, 12, 4,db=db)
        myRestraunt.book_table(12, 1, 12, 4,db=db)
        myRestraunt.book_table(12, 1, 12, 4,db=db)
        myRestraunt.book_table(12, 29, 12, 4,db=db)
        myRestraunt.book_table(12, 20, 12, 4,db=db)
        app.run()
    else:
        print "\n !!!! INVALID ACCESS or ACCESS DENIED!!!! \n"

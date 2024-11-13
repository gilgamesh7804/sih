import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
mycursor = mydb.cursor()
mycursor.execute("use sih;")

def format_data(data):
    data_dict = {}
    mycursor.execute("desc city_full_details;")
    temp = mycursor.fetchall()
    print(len(temp), len(data[0]))
    for i, j in zip(temp, data[0]):
        if str(j).find("?") != -1 and str(j)[0] != 'h':
            j = j.replace("?", "'")
        if str(j).find("~") != -1 and str(j)[0] != 'h':
            j = j.split("~")
        elif str(j).find("C:") != -1 and str(j)[0] != 'h':
            j = j.replace("C:\devel\\better_sih",'')
        # elif str(j).find(":") != -1 and str(j)[0] != 'h':
        #     print(
        #     j = j.split(":")
        #     j = [j[0].strip(), j[1].strip()]
        elif str(j).find("static") != -1 and str(j)[0] != 'h':
            j = j.lower()
        data_dict[i[0]]=j
    return data_dict

def get_city(city):
    q = f"select * from city_full_details where cityname='{city.title()}'"
    mycursor.execute(q)
    r = mycursor.fetchall()
    return format_data(r)




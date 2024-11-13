import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
mycursor = mydb.cursor()
mycursor.execute("use sih;")


def format_hidden_gems_data(data):
    data_dict = {}
    
    # Fetch column details of the table
    mycursor.execute("DESC hidden_gems;")
    temp = mycursor.fetchall()

    for i, j in zip(temp, data[0]):
        if isinstance(j, str):
            # Replacing all "?" with "'"
            if "?" in j:
                j = j.replace("?", "'")
            
            # Replacing "C:\\devel\\better_sih" in the path and keeping elements together
            if "C:" in j:
                j = j.replace("C:\\devel\\better_sih", '')
                j = j.strip()  # Only strip surrounding whitespace, don't split

        # If j is a list (like the paths in your case), join them together before modifications
        elif isinstance(j, list):
            joined_j = '\\'.join(j)  # Join the list into a single string with backslashes
            if "C:" in joined_j:
                joined_j = joined_j.replace("C:\\devel\\better_sih", '')
                joined_j = joined_j.strip()

            # Assign the joined and modified path back to j
            j = joined_j
        
        # Add to dictionary with column name as key
        data_dict[i[0]] = j

    return data_dict



def get_hidden_gem(gem):
    q = f"SELECT * FROM hidden_gems WHERE placename='{gem.title()}'"
    mycursor.execute(q)
    r = mycursor.fetchall()
    return format_hidden_gems_data(r)
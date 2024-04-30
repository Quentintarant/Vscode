import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rsb@2707",
  database="employeedb"
)
cursor = mydb.cursor()

def createTable():
    query = """
        create table person(
            id int primary key,
            first_name varchar(100),
            last_name varchar(100),
            city varchar(100)
        );
        """
    cursor.execute(query)
    mydb.commit()

def insertData():
    query = """
    INSERT INTO person (id, first_name, last_name, city) VALUES (%s, %s, %s, %s);
    """ 
    data = (2, "James", "Bond", "NY")
    cursor.execute(query, data)
    mydb.commit()

    print("record insert successfully")

def update():
    query = """
    update person set city= %s where id= %s
    """
    cursor.execute(query, ("mumbai", 1))
    mydb.commit()
    print("Updated successfully")

def delete():
    query = """
    delete FROM person where id= %s
    """
    cursor.execute(query, [1])
    mydb.commit()
    print("Deleted successfully")

def selectAll():
    cursor.execute("select * from person;")
    record = cursor.fetchone()
    print(f"id = {record[0]}, name= {record[1]+' '+record[2]}, city= {record[3]}")
    mydb.commit()

def main():
    print("1 Create table ")
    print("2 Insert Records ")
    print("3 Update Records ")
    print("4 Delete Records ")
    print("5 select Records ")
    userOption=int(input("Please enter the option"))

    if(userOption ==1):
        createTable()
    elif(userOption==2):
        insertData()
    elif(userOption==3):
        update()
    elif(userOption==5):
        selectAll()
    else:
        delete()
if __name__=="__main__": 
    main() 
    
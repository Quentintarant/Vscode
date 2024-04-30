import mysql.connector

conn=mysql.connector.connect(host='localhost', user='root', password='Rsb@2707', database='testpy')

cursor=conn.cursor()
def createtable():
    query = """
        create table name(
            id int primary key,
            first_name varchar(100),
            age int varchar(100),
            city varchar(100)
        );
        """
    cursor.execute(query)
    conn.commit()

def insertdata():
    query = """
    insert into name(int, first_name, city)  values(%s, %s, %s, %s);
    """
    data = (25, "Balaji", "Chennai" ) 

    cursor.execute(query, data)
    conn.commit()

    print("record insert successfully")

def update():
    query = """
    update name set city = %s WHERE id = %s
    """
    cursor.execute(query, ("Chennai", 1))
    conn.commit()
    print("updated successfully")

def delete():
    query = """
    DELETE from person where id = %s
    """
    cursor.execute(query, [1])
    conn.commit()
    print("deleted successfully")

def selectall():
    cursor.execute("select * from name;")
    record=cursor.fetchone()
    print("f id = {record[0]}, name = {record[1], + '' + record[2]}, city = {record[3]}")
    conn.commit()

def main():
    print("1 create table")
    print("2 insert records")
    print("3 update records")
    print("4 delete records")
    print("5 select records")
    useroption = int(input ("please enter the option"))

    if(useroption==1):
        createtable()
    elif(useroption==2):
        insertdata()
    elif(useroption==3):
        update()
    elif(useroption==5):
        selectall()
    else:
        delete()
if __name__=="__main__":
    main()
    
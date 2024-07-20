import sqlite3
import textwrap

""" 
creating shool.db 
    create table Course and Student by read sql file
    create query sql files 
        function for create_query_string
    open the file and read query sql file
    Raises:
        error_msg: _description_

    Returns:
        _type_: _description_
    """

# read sql file to read query and row
def create_query_string(sql_full_path): 
    with open(sql_full_path, 'r') as f_in: 
        lines = f_in.read() 
 
        # remove any common leading whitespace from every line     
        query_string = textwrap.dedent("""{}""".format(lines)) 
 
    return query_string  

def main():
    # Create database
    db =sqlite3.connect('data/school.db')
    # Get a cursor object to run queries.
    # cursor is like an alias to prevent typing db.cursor() all the time 
    cursor=db.cursor()
     #create table from sql file 
    create_course_table= '.\data\create_Course_table.sql'
    create_student_table= '.\data\create_Student_table.sql'
    table_list = [create_course_table,create_student_table]
    for table in table_list:
        print(table)
        with open(table, encoding="utf-8") as f:
            commands = f.read().split(';')

        for command in commands:
            cursor.execute(command)
            print(command)
            db.commit()
        
        
    # run sql file query and print data from table 
    try:  
        query_string= create_query_string('.\data\easiest_courses.sql')
        query_string1= create_query_string('.\data\\final_stage.sql')
        query_string2= create_query_string('.\data\julia_python.sql')
        query_string3 = create_query_string('.\data\machine_learning.sql')
        query_list = [query_string,query_string1,query_string2,query_string3]
        for index, query in enumerate(query_list):
            cursor.execute(query)
            print("*"*10,index, query, "*"*10,'\n')
            print("-"*20, 'QUERY DATA', "-"*20,'\n')
            
            rows = cursor.fetchall() # fetching all the  query data from the table
            for row in rows: # 
                if row :
                    print(row) # output the data 
            
            db.commit()
            print("\n",'-'*50)
    except Exception as error_msg:
        db.rollback()
        raise error_msg
    
    cursor.close()

if __name__ == "__main__":
    main()
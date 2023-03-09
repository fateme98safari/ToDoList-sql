import sqlite3


class Datebase:
    def __init__(self):
        self.con=sqlite3.connect("todo_list.db")
        self.cursor=self.con.cursor()
        self.cursor.execute("ALTER TABLE tasks ADD Priority INTEGER")
        self.con.commit()
        self.cursor.close()
    

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    

    
    def add_new_tasks(self , new_title , new_description , new_date_time):

        try:
            query=f"INSERT INTO tasks(title , description , date , time) VALUES ('{new_title}' , '{new_description}' ,'{new_date_time}') "
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def is_done(self,id):
         query=f"UPDATE tasks SET is_done=1 WHERE id='{id}'"
         self.cursor.execute(query)
         self.con.commit()





    def remove_tasks(self,id):
        query=f"DELETE FROM tasks WHERE id='{id}'"
        self.cursor.execute(query)
        self.con.commit()
       

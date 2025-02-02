import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",          
        user="root",               
        password="Anurag@2910",  
        database="chatbot_db"      
    )
    return connection

def store_chat_history(user_query, response):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "INSERT INTO chat_history (user_query, response) VALUES (%s, %s)"
    cursor.execute(query, (user_query, response))
    
    connection.commit()
    cursor.close()
    connection.close()
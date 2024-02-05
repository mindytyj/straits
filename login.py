import mysql.connector


# Function to connect to the MySQL database
def connect_db():
    conn = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    dbquery = conn.cursor()
    return conn, dbquery

# Function to check user credentials
def check_credentials(email, password):
    conn, dbquery = connect_db()
    dbquery.execute("SELECT * FROM Users WHERE Email = %s AND Password = %s", (email, password))
    user = dbquery.fetchone()
    conn.close()
    return user

# Main function for login
def login(email, password):
    user = check_credentials(email, password)

    if user:
        return f"Welcome, {user[0]}!<br>You are logged in as a {user[2]}"
    else:
        return "Invalid username or password."

if __name__ == "__main__":
    login()
import mysql.connector

# Function to connect to the MySQL database
def connect_db():
    conn = mysql.connector.connect(
        host="aws.connect.psdb.cloud",
        user="l1l50h3kzfg5au95tb1l",
        password="pscale_pw_SsfP659iLdnmQWE85VJuRj9TJTgXb4wfM42zNguojaP",
        database="straits"
    )
    dbquery = conn.cursor()
    return conn, dbquery

# Function to check user credentials
def check_credentials(username, password):
    conn, dbquery = connect_db()
    dbquery.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = dbquery.fetchone()
    conn.close()
    return user

# Main function for login
def login(username, password):
    print("Welcome to the login page!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = check_credentials(username, password)

    if user:
        print(f"Welcome, {user[0]}!")
        print(f"You are logged in as a {user[2]}")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    login()
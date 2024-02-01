import mysql.connector

# Function to connect to the MySQL database
def connect_db():
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (username VARCHAR(255) PRIMARY KEY, password VARCHAR(255), role VARCHAR(255))''')

    # Sample data - You can replace it with your actual data
    cursor.execute("INSERT IGNORE INTO users VALUES ('john', 'password123', 'staff')")
    cursor.execute("INSERT IGNORE INTO users VALUES ('emma', 'pass456', 'hr_officer')")
    cursor.execute("INSERT IGNORE INTO users VALUES ('alex', 'abc123', 'hr_supervisor')")

    conn.commit()
    return conn, cursor

# Function to check user credentials
def check_credentials(username, password):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Main function for login
def login():
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
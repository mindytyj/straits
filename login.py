from config import database


# Function to check user credentials
def check_credentials(email, password):
    dbquery = database.connection.cursor(dictionary=True)
    dbquery.execute("SELECT * FROM Users WHERE Email = %s AND Password = %s", (email, password))
    user = dbquery.fetchone()
    dbquery.close()
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
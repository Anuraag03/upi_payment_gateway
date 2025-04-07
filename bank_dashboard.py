import sqlite3

def view_users_and_transactions():
    conn = sqlite3.connect("bank_data.db")
    cursor = conn.cursor()

    print("=== Users and Their Details ===")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"Username: {user[0]}, Balance: ₹{user[3]}, Bank: {user[4]}, IFSC: {user[5]}, UID: {user[6]}, Mobile: {user[7]}, MMID: {user[8]}")
        print("  Transactions:")
        cursor.execute("SELECT * FROM transactions WHERE from_user = ?", (user[0],))
        transactions = cursor.fetchall()
        if transactions:
            for txn in transactions:
                print(f"    TXN ID: {txn[0]}, To Merchant: {txn[3]}, Amount: ₹{txn[5]}, Status: {txn[6]}, Timestamp: {txn[7]}")
        else:
            print("    No transactions found.")
        print()

    conn.close()

def view_merchants_and_transactions():
    conn = sqlite3.connect("bank_data.db")
    cursor = conn.cursor()

    print("=== Merchants and Their Details ===")
    cursor.execute("SELECT * FROM merchants")
    merchants = cursor.fetchall()
    for merchant in merchants:
        print(f"Name: {merchant[0]}, Balance: ₹{merchant[2]}, Bank: {merchant[3]}, IFSC: {merchant[4]}, MID: {merchant[5]}")
        print("  Transactions:")
        cursor.execute("SELECT * FROM transactions WHERE to_merchant = ?", (merchant[0],))
        transactions = cursor.fetchall()
        if transactions:
            for txn in transactions:
                print(f"    TXN ID: {txn[0]}, From User: {txn[1]}, Amount: ₹{txn[5]}, Status: {txn[6]}, Timestamp: {txn[7]}")
        else:
            print("    No transactions found.")
        print()

    conn.close()

if __name__ == "__main__":
    view_users_and_transactions()
    view_merchants_and_transactions()
# Rayan Fakhreddine

import sqlite3
from database.db import create_tables
from tkinter import Tk
from tkinter_backend import SchoolManagementGUI

def main():
    # Step 1: Connect to an SQLite database file, not the schema file
    conn = sqlite3.connect('database/school_management.db')

    # Step 2: Create tables if they don't exist
    create_tables(conn)
    
    # Step 3: Start the GUI application
    root = Tk()
    app = SchoolManagementGUI(root)
    root.mainloop()

    # Close the connection when done
    conn.close()

if __name__ == "__main__":
    main()

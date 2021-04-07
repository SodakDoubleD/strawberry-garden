import sqlite3


def migrate():
    """
    Apply any database migration scripts that haven't been applied.
    Scripts are applied in ascending order based on filename so changes
    can later changes can build off of previous ones.
    """
    # Create and/or connect to the StrawberryGarden database
    conn = sqlite3.connect('StrawberryGarden.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS migrations (
            primary_key INTEGER PRIMARY KEY,
            migration_name TEXT NOT NULL,
            migration_ran_on DATE
        )
    ''')

    conn.commit()


if __name__ == '__main__':
    migrate()

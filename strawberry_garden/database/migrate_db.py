import logging
import sqlite3

LOG = logging.getLogger(__name__)


def migrate():
    """
    Apply any database migration scripts that haven't been applied.
    Scripts are applied in ascending order based on filename so changes
    can later changes can build off of previous ones.
    """
    # Create and/or connect to the StrawberryGarden database
    conn = sqlite3.connect('StrawberryGarden.db')
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS migration (
                migration_id INTEGER PRIMARY KEY,
                migration_name TEXT NOT NULL,
                migration_ran_on DATE NOT NULL
            )
        ''')

        conn.commit()
    except Exception:
        LOG.exception('Failed to create migration table. Exiting.')
        return


if __name__ == '__main__':
    migrate()

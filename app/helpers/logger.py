from datetime import datetime, timezone
from app.db.sqlite import cursor, conn

def log(status, action, ip_address, username):
    query = """
        INSERT INTO activity_log VALUES (
            ?, ?, ?, ?, ?, ?
        )
    """
    cursor.execute(
        query, (
            None,
            status,
            action,
            ip_address,
            username,
            datetime.now(timezone.utc)
        )
    )
    conn.commit()
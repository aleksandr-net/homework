CREATE TABLE IF NOT EXISTS tasker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    header TEXT NOT NULL,
    description TEXT NOT NULL,
    start_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_date DATETIME NOT NULL,
    status INTEGER NOT NULL DEFAULT 0
)

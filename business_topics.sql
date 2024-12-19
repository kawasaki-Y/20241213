BEGIN TRANSACTION;
CREATE TABLE topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
INSERT INTO "topics" VALUES(1,'詳細','詳細','2024-12-19 15:42:27');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('topics',1);
COMMIT;

database = ["mongo","pg","mssql"]

def database_backup(db):
    print(f"backup for {db} database")

for db in database:
    database_backup(db)





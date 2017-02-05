# Database
db_uri_temp =  "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}"
SQLALCHEMY_DATABASE_URI =db_uri_temp.format(
        DB_USER="postgres",
        DB_PASS="",
        DB_ADDR="localhost",
        DB_NAME="test")


SQLALCHEMY_TRACK_MODIFICATIONS = True

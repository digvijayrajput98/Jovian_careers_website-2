
from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://29lzaxb8icqg:pscale_pw_8rh9TYVTudUaOCgPps801gveeWEYp7z_OsgWXvA07q4@je7hd4gvsmi0.ap-south-2.psdb.cloud/joviancareers?charset=utf8mb4"


engine = create_engine(db_connection_string,connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
}
                      )


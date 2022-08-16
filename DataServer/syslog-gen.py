
from elasticsearch import Elasticsearch
import random
from const import PORTMAP
from sys import exit
from time import sleep

#connect to the server
elastic_client= Elasticsearch('http://localhost:9200')

def main():
    
    port_list = []
    type_attack_list = []

    for port in PORTMAP:
        port_list.append(port)
        type_attack_list.append(PORTMAP[port])

    while True:
        port = random.choice(port_list)
        type_attack = random.choice(type_attack_list)
        cve_attack = 'CVE:{}:{}'.format(
                                random.randrange(1,2000),
                                random.randrange(100,1000)
                                )
        
        #define the query 
        query_body = 
        {
            "query":{
                "range":{
                    "@timestamp":{
                        "gte":"2015-08-04T11:00:00",
                        "lt":"2015-08-04T12:00:00"
                    }
                }
            }
        }
        
        id = randint(0,100)
        result = elastic_client.search(index='logstash-2022.07.13-000008', body=query_body, id= id)

        try:

            attack_data = '{},{},{},{},{},{}'.format(
                                                            attack_doc["_source"]["src_ip"],
                                                            attack_doc["_source"]["dest_ip"],
                                                            attack_doc["_source"]["src_port"],
                                                            attack_doc["_source"]["dest_port"],
                                                            type_attack,
                                                            cve_attack
                                                            )
        except :
            pass
        
       syslog(attack_data)
        print(attack_data)
        sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit() 


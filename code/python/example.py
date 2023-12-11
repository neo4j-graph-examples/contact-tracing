# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (p:Person {healthstatus:$status})-[v:VISITS]->(pl:Place)
 WHERE p.confirmedtime < v.starttime
 RETURN distinct pl.name as place LIMIT 20
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        status="Sick",
        database_="neo4j")
    for record in result.records:
        print(record['place'])

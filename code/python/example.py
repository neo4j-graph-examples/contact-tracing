# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>",
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (p:Person {healthstatus:$status})-[v:VISITS]->(pl:Place) 
WHERE p.confirmedtime < v.starttime 
RETURN distinct pl.name as place LIMIT 20
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      status="Sick").data())
  for record in results:
    print(record['place'])

driver.close()

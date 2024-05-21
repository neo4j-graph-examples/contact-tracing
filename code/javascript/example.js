// npm install --save neo4j-driver
// node example.js
const neo4j = require('neo4j-driver');
const driver = neo4j.driver('neo4j://<HOST>:<BOLTPORT>',
                  neo4j.auth.basic('<USERNAME>', '<PASSWORD>'), 
                  {});

const query =
  `
  MATCH (p:Person {healthstatus:$status})-[v:VISITS]->(pl:Place)
   WHERE p.confirmedtime < v.starttime
   RETURN distinct pl.name as place LIMIT 20
  `;

const params = {"status": "Sick"};

const session = driver.session({database:"neo4j"});

session.run(query, params)
  .then((result) => {
    result.records.forEach((record) => {
        console.log(record.get('place'));
    });
    session.close();
    driver.close();
  })
  .catch((error) => {
    console.error(error);
  });

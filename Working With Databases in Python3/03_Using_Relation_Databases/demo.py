from dataclasses import dataclass

#install psycoppg2 using pip install psycopg2-binary
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(
    host = "localhost", 
    database = "manager",
    user = "postgres",
    password = "password"
)

@dataclass
class Investment: 
    id: int
    coin: str
    currency: str
    amount: float

#no row factories. Have to use cursor factories
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictConnection)

create_investment_table = """
create table investment (
    id serial primar key, 
    coin varchar(32), 
    currency varchar(3),
    amount real
)
"""

add_bitcoin_investment = """
insert into investment (
    coin, currency, amount
) values (
    'bitcoin', 'USD', 1.0
);
"""

#generic statement
add_investment_template = """
insert into investment (
    coin, currency, amount
) values %s
"""

select_bitcoin_investment = "SELECT * FROM investment WHERE coin='bitcoin';"
select_all_investments = "SLECT * FROM investment;"

data = [
    ("ethereum", "GBP", 10.0),
    ("dogecoin", "EUR", 100.0)
]

cursor.execute(select_all_investments)

data = [Investment(**dict(row)) for row in cursor.fetchall()] #format as dictionaries

print(data)

for investment in data:
    print(investment.coin)

#psycopg2.extras.execute_values(cursor, add_investment_template, data)

connection.commit()

cursor.close()
connection.close()
import random
import datetime
import pandas

class Bernie:
    def __init__(self, num_transactions, num_clients, num_agents, offices, products):
        self.num_transactions = num_transactions
        self.num_clients = num_clients
        self.num_agents = num_agents
        self.offices = offices
        self.products = products
        self.transactions_list = []
        self.transactions_book: pandas.DataFrame = pandas.DataFrame(
            columns=["client_id", "agent_id", "office",
                     "product", "commission", "amount", "date"]
        )

    def generate_transaction(self) -> None:
        """
        Generate a fake JSON commissioned transaction between a client and an agent.

        Returns:
            transaction (dict): A fake JSON commissioned transaction.
        """
        # Generate random data
        client_id = random.randint(1, num_clients)
        agent_id = random.randint(1, num_agents)
        office = random.choice(offices)
        product = random.choice(list(products.keys()))
        commission = products[product]
        amount = random.randint(1000, 1000000)
        date = datetime.datetime(2020, 1, 1, 0, 0, 0) + datetime.timedelta(
            seconds=random.randint(0, 31536000))

        # Create transaction from random data
        transaction = {
            "client_id": client_id,
            "agent_id": agent_id,
            "office": office,
            "product": product,
            "commission": commission * amount,
            "amount": amount,
            "date": date
        }

        # Append transaction to transactions list
        self.transactions_list.append(transaction)

    def persist_transaction(self) -> None:
        """
        Write transactions list to DataFrame and persist to CSV file.
        """
        # Write transactions list to DataFrame
        self.transactions_book = pandas.DataFrame.from_dict(
            self.transactions_list)

        # Persist transactions to CSV file
        self.transactions_book.to_csv("transactions.csv", index=False)


if __name__ == "__main__":
    # The number of transactions to generate
    num_transactions = int(10e4)

    # The number of clients to generate
    num_clients = 200

    # The number of agents to generate
    num_agents = 10

    # Office locations
    offices = ["Nova Lima", "Brasilia", "Caxias do Sul",
               "Porto Alegre", "São Paulo", "Rio de Janeiro"]

    # Financial products available and respective commission
    products = {
        "Stocks": 0.01,
        "Bonds": 0.02,
        "Mutual Funds": 0.03,
        "ETFs": 0.04,
        "Options": 0.05,
        "Futures": 0.06,
        "Forex": 0.07,
        "Cryptocurrencies": 0.08,
        "Real Estate": 0.09,
        "Insurance": 0.10
    }

    # Generate a Bernie
    bernie = Bernie(num_transactions, num_clients,
                    num_agents, offices, products)

    # Generate fake JSON commissioned transactions and persist to CSV file
    for i in range(num_transactions):
        bernie.generate_transaction()

    # Persist transactions to DataFrame
    bernie.persist_transaction()

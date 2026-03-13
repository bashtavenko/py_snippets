"""Credit to  https://github.com/EricZheng0404/LibreSignal/tree/main"""


class Bank:

    def __init__(self):
        self.accounts = {}  # key: account_id (str), value: sum of deposits

    def create_account(self, timestamp: int, account_id: str) -> bool | None:
        if account_id in self.accounts:
            return False

        self.accounts[account_id] = 0
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None:
        if source_account_id == target_account_id:
            return None

        if source_account_id not in self.accounts or target_account_id not in self.accounts:
            return None

        if self.accounts[source_account_id] < amount:
            return None
        self.accounts[source_account_id] -= amount
        self.accounts[target_account_id] += amount
        return self.accounts[source_account_id]

from dataclasses import asdict
from typing import Optional

from server.accounts.account import AbstractAccountStore
from server.accounts.account import Account, AccountID
from server.db.base import Base
from server.db.tables import account_table


class AccountStore(Base, AbstractAccountStore):

    async def add(self, account: Account):
        async with self._database as connect:

            query = account_table.insert()

            await connect.execute(
                query=query,
                values=asdict(account)
            )

    async def find(self, account_id: AccountID) -> Optional[Account]:
        query = account_table.select().where(account_table.c.id == account_id)
        async with self._database as connect:
            row = await connect.fetch_one(query=query)
            if row is None:
                return None
            return self._row_as_account(row)

    async def delete(self, account_id: AccountID):
        query = account_table.delete().where(account_table.c.id == account_id)
        async with self._database as connect:
            await connect.fetch_one(query=query)

    async def update(self, account: Account):
        query = account_table.update().where(account_table.c.id == account.id)
        async with self._database as connect:
            await connect.execute(query=query, values=asdict(account))

    @staticmethod
    def _row_as_account(row):
        return Account(**dict(row))

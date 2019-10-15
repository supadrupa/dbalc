from server.accounts.account import AbstractAccountStore, Account, AccountID


class AccountService:
    def __init__(self, account_store: AbstractAccountStore):
        self._account_store = account_store

    async def add(self, account: Account):
        await self._account_store.add(account=account)

    async def find(self, account_id: AccountID):
        return await self._account_store.find(account_id=account_id)

    async def delete(self, account_id: AccountID):
        await self._account_store.delete(account_id)

    async def update(self, account: Account):
        return await self._account_store.update(account)

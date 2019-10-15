import pytest
import asyncio
from uuid import uuid4

from databases import Database

from server.accounts.service import AccountService, Account, AccountID
from server.db.account_store import AccountStore

account_service = AccountService(
    account_store=AccountStore(
        database=Database("postgresql://dbalc:dbalc@localhost:5432/dbalc")
    )
)

account = Account(
    id=AccountID(uuid4()),
    avatar="avatar",
    proxy="proxy",
    client_id=123
)


@pytest.mark.asyncio
async def test_service():

    await account_service.add(account)
    res = await account_service.find(account.id)
    assert res == account

    account.domain = "domain"
    await account_service.update(account)
    res = await account_service.find(account.id)
    assert res == account

    await account_service.delete(account.id)

    res = await account_service.find(account.id)
    assert res is None


if __name__ == '__main__':
    pytest.main()

from __future__ import annotations

import abc
import datetime
from dataclasses import dataclass, field
from typing import NewType, Optional
from uuid import UUID

AccountID = NewType("AccountID", UUID)


@dataclass
class Account:
    id: AccountID
    avatar: str
    proxy: str
    client_id: int
    created_at: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(tz=datetime.timezone.utc)
    )
    domain: Optional[str] = None
    position: Optional[int] = None
    is_archived: bool = False


class AbstractAccountStore(abc.ABC):
    @abc.abstractmethod
    async def add(self, account: Account):
        pass

    @abc.abstractmethod
    async def find(self, account_id: AccountID) -> Optional[Account]:
        pass

    @abc.abstractmethod
    async def delete(self, account_id: AccountID):
        pass

    @abc.abstractmethod
    async def update(self, account: Account):
        pass

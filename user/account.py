import uuid
from typing import List

class Account:
    def __init__(self, account_id: uuid.UUID, account_name: str, address_chain: dict[str,List[str]]):
        self.account_id = account_id
        self.account_name = account_name
        self.address_chain = address_chain
    
    def get_name(self) -> str:
        return self.name
    
    def get_account_id(self) -> str:
        return self.account_id
    
    def get_address_chain(self) -> dict[str,List[str]]:
        return self.address_chain
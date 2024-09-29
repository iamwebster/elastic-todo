from abc import ABC, abstractmethod


class AbstractReporsitory(ABC):
    
    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def get_single(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod 
    async def update(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod 
    async def delete(self, **kwargs):
        raise NotImplementedError
    
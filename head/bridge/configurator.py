from head.interfaces.abstracts.interface import IAbstractFabric
from head.interfaces.fabrics.interface import IConcreteFabric


class BridgeConfigurator:

    def __init__(self, abstractFabric: IAbstractFabric, fabricKey: str, productKey: str) -> None:
        self._abstractFabric: IAbstractFabric = abstractFabric
        self._fabricKey: str = fabricKey
        self._productKey: str = productKey

    @property
    def abstractFabric(self) -> IAbstractFabric:
        return self._abstractFabric

    @property
    def fabricKey(self) -> str:
        return self._fabricKey

    @property
    def productKey(self) -> str:
        return self._productKey

    def produceFabric(self) -> IConcreteFabric:
        return self.abstractFabric.getFabric(self.fabricKey)

    def produceProduct(self) -> object:
        return self.produceFabric().getProduct(self.productKey)

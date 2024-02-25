import datetime
from dataclasses import dataclass, field

from .const import (
    ICON_LIST,
    NAME_LIST,
)

@dataclass
class RenoWebAddressInfo:
    """Represent RenoWeb address info."""
    address_id: str
    kommunenavn: str
    vejnavn: str
    husnr: str

@dataclass(order=True)
class RenoWebPickupData:
    """Represent RenoWeb pickup data."""
    sort_index: int = field(init=False, repr=False)
    id: int
    materielnavn: str
    ordningnavn: str
    toemningsdage: str
    toemningsdato: str
    toemningsint: int
    mattypeid: int
    antal: int
    vejnavn: str
    fractionid: int
    modulId: int

    @property
    def icon(self) -> str:
        """Return the icon."""
        if self.ordningnavn is None:
            return None

        for key, value in ICON_LIST.items():
            if self.ordningnavn == key:
                return value
        return "mdi:delete-empty"

    @property
    def name(self) -> str:
        """Return the name."""
        if self.ordningnavn is None:
            return None

        for key, value in NAME_LIST.items():
            if self.ordningnavn == key:
                return value
        return self.ordningnavn

    @property
    def pickup_date(self) -> datetime.date:
        """Return the pickup date."""
        if self.toemningsdato is None:
            return None

        if self.toemningsdato == "Ingen tømningsdato fundet!":
            return None

        index = self.toemningsdato.rfind(" ")
        return datetime.datetime.strptime(self.toemningsdato[index+1:], "%d-%m-%Y").date()

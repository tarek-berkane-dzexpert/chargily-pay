from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Address:
    country: Optional[str] = ""
    state: Optional[str] = ""
    address: Optional[str] = ""


@dataclass
class Customer:
    name: str
    email: str
    address: Address = None
    metadata: list = field(default_factory=list)


@dataclass
class Product:
    name: str
    description: Optional[str] = None
    images: list[str] = None
    metadata: list[dict] = field(default_factory=list)


@dataclass
class Price:
    amount: int
    currency: str
    product_id: str
    metadata: list[dict] = field(default_factory=list)


@dataclass
class CheckoutItem:
    price: str
    quantity: int


@dataclass
class Checkout:
    items: CheckoutItem
    success_url: str
    failure_url: str = None
    customer_id: str = None
    description: str = None
    locale: str = None
    pass_fees_to_customer: bool = None
    metadata: list[dict] = field(default_factory=list)


@dataclass
class PaymentItem:
    price: str
    quantity: int
    adjustable_quantity: bool = None

@dataclass
class PaymentLink:
    name: str
    items : list[PaymentItem]
    after_completion_message:str = None
    locale : str = None
    pass_fees_to_customer : bool = None
    metadata : list[dict] = field(default_factory=list)
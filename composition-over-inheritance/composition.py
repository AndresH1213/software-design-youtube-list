"""
Very advanced Employee management system with composition design.
Composition over inheritance.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Comission(ABC):
    """Represents a generic comission"""

    @abstractmethod
    def get_payment(self) -> float:
        """Computes the comission to be paid out."""


@dataclass
class ContractComission(Comission):
    """Represents a commission."""

    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        """Computes the comission to be paid out."""
        return self.commission * self.contracts_landed


class Contract:
    """Respresents a contract and payment process for a particular employee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay and employee under this contract."""


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    id: int
    contract: Contract
    comission: Optional[Comission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.comission is not None:
            payout += self.comission.get_payment()
        return payout


@dataclass
class HourlyContract(Contract):
    """Contract type for an employee that's paid based on number of worked hours."""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedContract(Contract):
    """contract type for an employee that's paid based on a fixed monthly salary."""

    montly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return self.montly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """contract type for an employee that's paid based on freelancer basis."""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(montly_salary=5000)
    sarah_comission = ContractComission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", id=47832, contract=sarah_contract, comission=sarah_comission)
    print(
        f"{sarah.name} landed {sarah_comission.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()

from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast
@dataclass
class Regulator:
    reglator_int: int = None
    provided_length: int = None

    @property
    def test_reglator_int(self):
        return self.test_reglator_int

    @test_reglator_int.setter
    def test_reglator_int(self, reglator_int: int):
        self.reglator_int = reglator_int

    @property
    def test_provided_length(self):
        return self.test_provided_length

    @test_provided_length.setter
    def test_provided_length(self, provided_length: int):
        self.provided_length = provided_length

@dataclass
class DeRegulator:
    reglator_int: int = None
    provided_length: int = None

    @property
    def test_reglator_int(self):
        return self.test_reglator_int

    @test_reglator_int.setter
    def test_reglator_int(self, reglator_int: int):
        self.reglator_int = reglator_int

    @property
    def test_provided_length(self):
        return self.test_provided_length

    @test_provided_length.setter
    def test_provided_length(self, provided_length: int):
        self.provided_length = provided_length

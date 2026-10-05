from pydantic import BaseModel, Field

from typing import Literal

class PrediccionInput(BaseModel):
    Pclass: int = Field(
        description='1 = First Class, 2 = Second class, 3 = Third class',
        ge=1,
        le=3
    )
    Name: str = Field(
        description='Passenger name. Must have the title and dot. Like "Mr."'
    )
    Sex: Literal['male', 'Female'] = Field(
        description='Passenger sex'
    )
    Age: float | None = Field(
        default=None,
        description='Passenger age',
        ge=0
    )
    SibSp: int = Field(
        description='Number of siblings or spouses aboard the Titanic',
        ge=0
    )
    Parch: int = Field(
        description='Number of parents or children aboard the Titanic',
        ge=0
    )
    Fare: float = Field(
        description='Passenger fare'
    )
    Embarked: Literal['C', 'Q', 'S'] = Field(
        description='C = Cherbourg, Q = Queenstown, S = Southhampton'
    )

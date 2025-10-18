from pydantic import BaseModel, Field
from typing import Literal

class CustomerData(BaseModel):

    CreditScore : int =Field(description='Credit Score of the customer')
    Age : int = Field('Age of the Custmer (18-100)', ge= 18, le=100)
    Tenure : int = Field('Tenure of the customer', ge=0, le=10)
    Balance : float = Field('Account Balance', ge= 0)
    NumOfProducts : int = Field('Number of products (1-4)',ge=0, le=4 )
    HasCrCard: Literal[0,1] = Field('Customer has credit card(no=0, yes=1)')
    IsActiveMember: Literal[0,1] = Field('Customer is Active (no=0, yes=1)')
    EstimatedSalary	: float = Field('Customer Estimated Salary', ge=0)
    Geography: Literal['France', 'Germany', 'Spain'] = Field('Cutomer Geography (France, Germany, Spain)')
    Gender : Literal['Male', 'Female'] = Field('Cusomer Gender (Male, Female)')


from pydantic import BaseModel, ConfigDict, Field

class ProductCreate(BaseModel):
    product_name: str = Field(...,min_length=1, max_length=100)
    category: str = Field(...,min_length=1, max_length=100)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., gt=0)

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    product_id: int
    product_name: str
    category: str
    quantity: int
    price: float


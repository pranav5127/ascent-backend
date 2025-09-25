from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from ascentdb.app.database import get_db
from ascentdb.app.schemas.resources import ResourceBase, ResourceResponse
from ascentdb.app.crud.resources import add_resource, get_resource, get_resources_by_class, update_resource, delete_resource

router = APIRouter(prefix="/resources", tags=["Resources"])

@router.post("/", response_model=ResourceResponse)
def add_resource_endpoint(resource: ResourceBase, db: Session = Depends(get_db)):
    return add_resource(db, resource)

@router.get("/{resource_id}", response_model=ResourceResponse)
def get_resource_endpoint(resource_id: UUID, db: Session = Depends(get_db)):
    res = get_resource(db, resource_id)
    if not res:
        raise HTTPException(status_code=404, detail="Resource not found")
    return res

@router.get("/class/{class_id}", response_model=List[ResourceResponse])
def get_resources_by_class_endpoint(class_id: UUID, db: Session = Depends(get_db)):
    return get_resources_by_class(db, class_id)

@router.put("/{resource_id}", response_model=ResourceResponse)
def update_resource_endpoint(resource_id: UUID, update_data: dict, db: Session = Depends(get_db)):
    res = update_resource(db, resource_id, update_data)
    if not res:
        raise HTTPException(status_code=404, detail="Resource not found")
    return res

@router.delete("/{resource_id}", response_model=ResourceResponse)
def delete_resource_endpoint(resource_id: UUID, db: Session = Depends(get_db)):
    res = delete_resource(db, resource_id)
    if not res:
        raise HTTPException(status_code=404, detail="Resource not found")
    return res

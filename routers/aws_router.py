from fastapi import APIRouter,HTTPException
from services.aws_services import get_bucket_info,get_instances_info

router = APIRouter()
@router.get("/s3",status_code=200)
def get_buckets():
    try:
        buckets = get_bucket_info()
        return buckets
    except:
        raise HTTPException(
            status_code=500,
            detail = "Internal Server Error"
        )  
@router.get("/ec2",status_code=200)
def get_instance():
    try:
        instances = get_instances_info()
        return instances
    except:
        raise HTTPException(
            status_code=500,
            detail = "Internal Server Error"
        )    
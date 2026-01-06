from fastapi import FastAPI #importing FastAPI Class
from routers import metrics,aws_router
app = FastAPI(
    title = "Internal App Utilities API",
    description="This is an internal API utilities app for monitoring metrics",
    version = "1.1.0",
    doc_url= "/docs",
    redoc_url= "/redoc"
)
@app.get("/")
def utility_app():
    return{"message":"App Utilities API is running"}
app.include_router(metrics.router)
app.include_router(aws_router.router, prefix="/aws")
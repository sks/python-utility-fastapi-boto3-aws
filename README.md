\# python-utility-fastapi-boto3-aws



Internal Python utility APIs built using FastAPI and boto3 for AWS operations and system metrics.

This project is designed for DevOps and cloud automation use cases.



---



\## Features



\- FastAPI-based REST APIs

\- AWS utilities using boto3

\- System and application metrics endpoints

\- Clean, modular project structure

\- Single entry point for application startup



---



\## Project Structure



python-utility-fastapi-boto3-aws/

│

├── app/

│ └── api.py # FastAPI application setup

│

├── routers/ # API route definitions

│ ├── metrics.py

│ └── aws\_router.py

│

├── services/ # Business logic layer

│ ├── metrics\_service.py

│ └── aws\_services.py

│

├── main.py # Application entry point

├── requirements.txt

├── README.md





---



\## Tech Stack



\- Python 3.9+

\- FastAPI

\- Uvicorn

\- boto3 (AWS SDK for Python)



---



\## Setup Instructions



\### 1. Clone the repository



```bash

git clone https://github.com/<your-username>/python-utility-fastapi-boto3-aws.git

cd python-utility-fastapi-boto3-aws



2\. Create and activate virtual environment

python -m venv venv



For Windows -  Run this command

venv\\Scripts\\activate



For Linux / macOS -  Run this command

source venv/bin/activate



3\. Install dependencies

pip install -r requirements.txt



---Running the Application---

Recommended (entry point) - 
Run python main.py
This is the only recommended way to run the application locally.


🌐 API Access



Once the server is running:



Base URL



http://127.0.0.1:8000/





Swagger UI



http://127.0.0.1:8000/docs





ReDoc



http://127.0.0.1:8000/redoc





Example Endpoints

Method	Endpoint	Description

GET	/	Health check

GET	/metrics	System metrics

GET	/aws/\*	AWS utility endpoints


------------------------------------------------------------


For a new user, AWS must be configured locally before your FastAPI + boto3 app can show AWS resources (like EC2 instances).



🔑 Why AWS connection is required



Your app uses boto3, which does not magically connect to AWS.

boto3 works only when it can find valid AWS credentials, such as:

Access Key

Secret Key

Region

(Optional) Session token

Without these → no instances, no AWS data



How a new user should connect AWS (RECOMMENDED way)

Step 1: Install AWS CLI



Check if aws is installed:

aws --version



If not installed, install from AWS official site.

Step 2: Configure AWS credentials



Run:

aws configure



Enter:



AWS Access Key ID:     \*\*\*\*\*\*\*\*\*\*\*\*

AWS Secret Access Key: \*\*\*\*\*\*\*\*\*\*\*\*

Default region name:  <Press Enter>

Default output format: <Press Enter>





This creates credentials here:



~/.aws/credentials

~/.aws/config


Step 3: Verify AWS access

aws ec2 describe-instances



If this works → your app will work ✅


🔐 IAM permissions (VERY IMPORTANT)



The IAM user/role must have permissions like:



{

&nbsp; "Effect": "Allow",

&nbsp; "Action": \[

&nbsp;   "ec2:DescribeInstances",

&nbsp;   "ec2:DescribeVolumes",

&nbsp;   "ec2:DescribeSnapshots"

&nbsp; ],

&nbsp; "Resource": "\*"

}





Without permissions → boto3 will fail with AccessDenied.


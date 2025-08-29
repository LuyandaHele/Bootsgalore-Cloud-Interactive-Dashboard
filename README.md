Project Title: BootsGalore Cloud Interactive Dashboard

Project Description
This project is a real-world inspired cloud engineering project designed to transform raw client data such as preferences when it comes to football boots, stud type preferences or size preferences
into actionable business insights. This project mirrors a production-grade architecture by leveraging AWS cloud services to a build a complete data pipeline and interactive dashboard. It was inspired 
by a online football boot store where understanding customer preferences , sale trends amd product performance is critcal for business growth.

What This Project Demonstrates
- Data Ingestion & Storage: Upload raw CSV files into an Amazon S3 bucket for centralized, durable storage.
- ETL Pipeline: An AWS Lambda (Python) function automatically cleans and transforms incoming data before inserting it into a cloud database.( A trigger was implemented for this)
- Data Storage: Processed data is stored in DynamoDB (NoSQL) for fast lookups and scalable access.
- Interactive Dashboard: A Streamlit Dashboard provide live insights into brand preferences, football size preferences and stud type preferences.
- Cloud Deployment: The dashboard is hosted on AWS EC2, making it accessible as a live cloud application.
- Security & Monitoring: IAM policies enforce least-privilage access, while CloudWatch logs track pipeline execution and to identify any erros throughout the process.
- CI/CD Workflow: Github Actions + AWS deployment commands ensure continous delivery and version control.

Why This Project Matters
This project solves a real business problem turning raw data into a business intelligence with cloud technologies. It reflects the same skills and tools used in enterprise-level cloud environments, from
event-driven ETL to secure cloud deployment. By designing and implementing this end-to-end I gained hands-on experience in cloud architecture, engineering and DevOps workflows, while building
a solution that could directly support business decision-making.

Architecture Diagram 
This diagram shows the overall flow of the Cloud Interactive Dashboard project: 
![BootsGalore Cloud Interactive Dashboard Architecture Diagram](https://github.com/LuyandaHele/Bootsgalore-Cloud-Interactive-Dashboard/blob/main/BootsGalore-Cloud-Interactive-Dashboard/Architecture%20Diagram/AWS%20Interactive%20Cloud%20Dashboard%20Project%20(2).png)
Architecture Diagram Explanation : High-level architecture showing S3 ingestion, Lambda ETL, DynamoD storage and Streamlit dashboard hosted on EC2.

Tech Stack Used
Cloud Services:
-Amazon S3: Centralized storage for raw CSV files.
-Amazon Lambda: Event-driven ETL function to clean and transform incoming data.
-DynamoDB: NoSQL database to store processed data for fast lookups. 
-Amazon EC2: Hosts the Streamlit dashboard as a live cloud application. 
-IAM & Security Groups: Enforces least-privilege access and manages secure network connectivity.
-CloudWatch Logs: Monitoring and logging of ETL and dashboard processes. 
Programming & Analytics:
-Python: Core programming language for ETL,data processing and dashboard development.
-Pandas: Data manipulation and cleaning.
-Matplotlib / Streamlit Charts: Interactive and visually appealing dashboards.
-Streamlit: Framework to build and deploy the interactive web dashboard.
Version Control & CI/CD:
-Git & Github: Source code management and version control.
-Github Actions: Automates deployment workflows and continous intergration.    

Screenshots of Workflow:
![S3 Bucket](https://github.com/LuyandaHele/Bootsgalore-Cloud-Interactive-Dashboard/tree/main/BootsGalore-Cloud-Interactive-Dashboard/S3%20Bucket%20%26%20File%20Uploaded)
![ETL Lambda Function](https://github.com/LuyandaHele/Bootsgalore-Cloud-Interactive-Dashboard/tree/main/BootsGalore-Cloud-Interactive-Dashboard/ETL)
![DynamoDB Table](https://github.com/LuyandaHele/Bootsgalore-Cloud-Interactive-Dashboard/tree/main/BootsGalore-Cloud-Interactive-Dashboard/DynamoDB)
![Streamlit Dashboard](https://github.com/LuyandaHele/Bootsgalore-Cloud-Interactive-Dashboard/tree/main/BootsGalore-Cloud-Interactive-Dashboard/Deployment%20%26%20Terminal%20txt)
![EC2](https://github.com/LuyandaHele/Bootsgalore-Cloud-Interactive-Dashboard/tree/main/BootsGalore-Cloud-Interactive-Dashboard/EC2)

BootsGalore Cloud Interactive Dashboard Repository Folder Structure:
BootsGalore-Cloud-Interactive-Dashboard/
|--Architecture diagram/ (Project Architecture diagram)
|--CloudWatch Logs/ (Sample logs from AWS Lambda execution)
|--Dashboard/ (Streamlit interactive dashboard app.py)
|--Data/ (CSV data)
|--Deployment & Terminal txt/ (Deployment commands, terminal outputs)
|--DynamoDB/ (DynamoDB table screenshots / exports)
|--ETL function/ (AWS Lambda ETL function (lambda_function.py))
|--Policies/ (Iam policies used for access control)
|--S3 Bucket & File Uploaded/ (Screenshots of files stored and uploaded to s3 and bucket)
|--README.md (Project overview and documentation) 

Lessons Learnt 
1.) Json Policy : Misconfigured S3 permissions that blocked Lambda; solved by refining JSON policy.
2.) EC2 VS Local Terminal : Learned to differentiate commands for local uploads (scp) vs remote execution (ssh).
3.) Code Reliability : Importance of writing clean, tested Python code to ensure Streamlit and ETL worked.

Video Walkthrough Link : (Link)

Author / Contact
Luyanda Hele 
Aspiring Cloud Engineer / Cloud Data Engineer 
www.linkedin.com/in/luyanda-hele-8999761b4 | https://github.com/LuyandaHele/Bootsgalore-Cloud-Interactive-Dashboard/new/main?filename=README.md | Email : luyandalui576@gmail.com







 

 

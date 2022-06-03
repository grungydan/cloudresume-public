## Welcome to the code behind my take on the Cloud Resume Challenge
#### Original project spec by Forrest Brazael, which can be found at https://cloudresumechallenge.dev

***
### Project Descriptoin
The end product of the challenge is a cloud-based and cloud-powered resume utilizing several AWS services as well as a healthy dose of IaC and CI/CD workflows. 

***
![arch-diag](https://user-images.githubusercontent.com/45023799/171901916-c5f378ed-2dd1-4d6b-b976-c0d0a9c615d8.png)
***
### The Website
The front end is built using HTML/CSS with some JS to fetch and update the visitor count. This was the first part that I worked on, and as the project author predicts, the part that took the least amount of time. The files for the site are hosted from a S3 Bucket, which are then distributed using CloudFront, with DNS powered by Route53. 
### The Counter
This is where I entered new territory. The data is stored in a DynamoDB table and powered by a Lambda function written in Python, which is accessed via a REST API built in AWS API Gateway. When the website loads, the page's JS function runs a fetch against the API, which in turn uses a GET method call against the Lambda function, which updates an atomic counter in DynamoDB and responds with the new value, which the JS displays on the site. 
### CI/CD
Continuing to delve deeper into unfamiliar lands, it was time to implement some automation. Reading through the challenge, it was clear that there were several approaches I could take here, but there were two that I wanted to look at specifically. So rather than pick one, I used both. On checking in any changes to the front end files (HTML/CSS/JS), AWS CodePipeline kicks off and replaces the contents of the hosting S3 Bucket with the new files. On checking in new backend code, things get more interesting. GitHub Actions triggers a workflow which rebuilds and then redeploys the backend using AWS SAM (Serverless Application Model), which offers a sort of shorthand way of building infrastructure using AWS CloudFormation. At the end of each run, I'm left with a CloudFormation stack consisting of a REST API in APIGW, a Python Lambda function, and my table in DynamoDB. Sweet.
### My Takeaways
It's hard to briefly summarize just how much I learned working on this project. Certainly I got to delve into many fantastic service offering from AWS. I also got to use Python with the excellent and well documemented boto3 framework from Amazon. I think the best way to encapsulate what I have taken away from this is that I now have a much better understanding of the nuts and bolts of "serverless" and the development of an application developed in the loosely coupled microservice architecture. It's one thing to understand the theory or "idea" of such a thing, but to actually put your hands to the keyboard and build it is another thing entirely. I enjoyed this challenge, even when fixing one error only meant being faced with another. I can't wait to build something else!

```mermaid
graph LR
    A[Local Python Script] -->|requests| B[API Gateway]
    B --> C[Lambda Function]
    C --> D[Bedrock API]
    C --> E[S3 Bucket]
    D --> C
    B -->|Summary Output| A
```

# Apps on AWS

## Streamlit host on EC2
- *目的*就是在EC2上host，这很简单
- 准备Streamlit的Github代码库（只有app和requirement）
- 创建基础EC2:首次需要rsaKey，但是可以从console连接(ubuntu)
- Port端口mapping：8501，也就是添加到SG白名单
- 启动EC2跑以下命令：

```shell
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget -y
git clone "Your-repository"
sudo apt install python3-pip
pip3 install -r requirements.txt
#Temporary running
python3 -m streamlit run app.py
#Permanent running(在切断连接后持续运行)
nohup python3 -m streamlit run app.py
```

- 然后就可以通过公共IP访问：<ip-address>:8501

## Streamlit host on Docker
- *目的*是使用EC2作为环境，进行整个docker封装和push过程
- 准备Streamlit的Github代码库（文件夹内容）
- 创建基础EC2:首次需要rsaKey，但是可以从console连接(ubuntu)
- Port端口mapping：8501，也就是添加到SG白名单
- 启动EC2跑以下命令：
```shell
sudo apt-get update -y
sudo apt-get upgrade
#Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
git clone "your-project"
docker build -t <your-docker-hub-username>/stapp:latest .
docker images -a
docker run -d -p 8501:8501 <your-docker-hub-username>/stapp
docker ps
docker stop container_id
docker rm $(docker ps -a -q)
docker login
docker push <your-docker-hub-username>/stapp:latest
docker rmi <your-docker-hub-username>/stapp:latest
docker pull <your-docker-hub-username>/stapp
```

## summary-contents

- *Lambda Function*：
- 创建LambdaFunction，配置timeout时长为APIGateway时长29秒用于测试
- 创建LambdaFunction的IAMrole：CloudWatch，S3，Bedrock的权限
- 部署Function，输入是日语，需要解决字符解码问题
- 最新的python版本支持bedrock-runtime，无需解决问题

- *S3*：
- 创建用于文件输出的bucket

- *API Gateway*：
- 创建以Lambda Function为后端的dev-stage环境
- 用resource policy限制ip访问：暂时安全起见将所有的ip屏蔽了

- *test.py*：
- 从本地使用test代码call api，可以直接返回结果
- 也可以在S3中确认到结果文件
- 疑点，本地可以解析为日语，但是s3中下载的是英语，最后一次为日语

- *使用Lambda Function URL*
  - 由于API Gateway有29秒限制，所以使用了Lambda Function URL功能呢
  - 这个功能无法设置ip限制，所以通过添加 code 逻辑限制 ip 访问
  - 这样就不需要使用API Gateway了

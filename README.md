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

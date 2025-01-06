# Install Java
## Install
```
sudo apt update
sudo apt install openjdk-11-jdk
```
## Check
```
java -version
javac -version
```

## Setting JAVA_HOME
```
sudo vim ~/.bashrc
```
```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

# Install maven
## Install
```
sudo apt update
sudo apt install maven
```
## Check
```
mvn -version
```

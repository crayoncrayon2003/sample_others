mkdir -p ./jenkins_home ./jenkins_home/workspace ./jenkins_home/workspace/case3

cat <<EOL > ./jenkins_home/workspace/case3/script1.py
print("Hello, Jenkins 1")
EOL

cat <<EOL > ./jenkins_home/workspace/case3/script2.py
print("Hello, Jenkins 2")
EOL

cat <<EOL > ./jenkins_home/workspace/case3/script3.py
print("Hello, Jenkins 3")
EOL

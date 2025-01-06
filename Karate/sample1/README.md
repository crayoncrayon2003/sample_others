# create sample project
```
mvn archetype:generate \
-DarchetypeGroupId=com.intuit.karate \
-DarchetypeArtifactId=karate-archetype \
-DarchetypeVersion=0.7.0 \
-DgroupId=example -DartifactId=example-karate
```

# build and run
```
cd example-karate
mvn clean test
```

# check test report
```
target/surefire-reports/TEST-examples.users.users.html
```

# check test code
```
src/java/examples/users/users.feature
```

# Root Dir
```
cd sampl2/project
```

# Exec
## Build
```
mvn compile
```
## Run
```
mvn exec:java -Dexec.mainClass=com.example.HttpServerExample
```

# build and run
## Run all
```
mvn clean test
```

## Run individually
```
mvn -Dtest=HelloApiTest test
```

```
mvn -Dtest=DataApiTest test
```

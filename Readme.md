### Prerequisites
This project requires Docker and docker-compose

See the [Docker website](http://www.docker.io/gettingstarted/#h_installation) for installation instructions.

To install docker-compose do ```pip install docker-compose```

### Pre-commit initialize
1. pip install pre-commit
2. pre-commit install

### Pre-commit run before commiting changes
```
pre-commit run --all-files
```

### To run development server
1. Copy the file ```environment/template``` to ```environment/dev```
2. Build the docker images
    ```docker-compose build```
3. Run the containers in background ```docker-compose up -d```
4. Access the application at [http://localhost:8000](http://localhost:8000)
5. To stop the containers do ```docker-compose down```


### To use Py-test for testing

1. First run ```docker-compose build``` , since new modules/packages will be there (only first time).
2. Run the containers in background ```docker-compose -f docker-compose.test.yml up -d```

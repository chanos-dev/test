#### Install
```shell
pip install locust

locust -V
-> locust x.x.x
```

#### Script Example
##### HttpUser
```python
from locust import HttpUser, task

class User(HttpUser):
    @task
    def get(self):
        self.client.get('/WeatherForecast')
```

##### TaskSet
```python
from locust import HttpUser, task, TaskSet

class PostTask(TaskSet):
    @task
    def post(self):
        body = {
            'data': 'hello, world!'
        }

        self.client.post('/WeatherForecast', json=body) 

class User(HttpUser):
    tasks = [PostTask]
```
##### SequentialTaskSet
```python
from locust import HttpUser, task, SequentialTaskSet

class SequentialTask(SequentialTaskSet):
    @task
    def get(self):
        self.client.get('/WeatherForecast')
        
    @task
    def post(self):
        body = {
            'data': 'hello, world!'
        }

        self.client.post('/WeatherForecast', json=body) 

class User(HttpUser):
    tasks = [SequentialTask]
```

#### Execute
```shell
locust -f ./{locust_script}.py

# locust web port 변경
locust -f ./{locust_script}.py --web-port={port_number}
```
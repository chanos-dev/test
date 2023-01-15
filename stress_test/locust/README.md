#### Install
```shell
pip install locust

locust -V
-> locust x.x.x
```

#### Script Example
##### SSL Error
```python
from locust import HttpUser, task,
class User(HttpUser):
    @task
    def get(self):
        self.client.get('/WeatherForecast')

    def on_start(self):
        self.client.verify = False
```

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

##### Custom arguments
```python
from locust import HttpUser, task, events

@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument('--test', type=str, help='test data')

class User(HttpUser):
    @task
    def get(self):
        print(self.environment.parsed_options.test)
        self.client.get('/WeatherForecast')
```

#### Execute
```shell
locust -f ./{locust_script}.py

# locust web port 변경
locust -f ./{locust_script}.py --web-port={port_number}

# custom argument
locust -f ./{locust_script}.py --test=test_data

# master & worker
locust -f ./{locust_script}.py --master
locust -f ./{locust_script}.py --worker --master-host=127.0.0.1

# run without WEB UI
locust -f ./{locust_script}.py -H http://localhost:5032 -u 10 -r 1 -t 10s --headless
```
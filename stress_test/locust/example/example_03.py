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
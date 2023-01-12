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
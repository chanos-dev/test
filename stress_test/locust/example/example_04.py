from locust import HttpUser, task, events

@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument('--test', type=str, help='test data')
    parser.add_argument('--hello-world', type=str, help='test hyphen variable')

class User(HttpUser):
    @task
    def get(self):
        print(self.environment.parsed_options.test)
        print(self.environment.parsed_options.hello_world)
        self.client.get('/WeatherForecast')
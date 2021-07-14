from locust import TaskSet, task, between
from locust.user.task import TaskSet
from memcached import MemcachedLocust


class UserBehavior(TaskSet):
    @task(1)
    def set(self):
        self.client.random_set()

    @task(10)
    def get(self):
        self.client.random_get()


class WebsiteUser(MemcachedLocust):
    tasks = [UserBehavior]
    wait_time = between(0, 1)
    host = "cache"
    max_set_size = 10000
    number_of_keys = 100
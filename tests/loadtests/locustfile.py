from locust import HttpUser, task, between


class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.user_id = 1
        self.headers = {
            "Content-Type": "application/json"
        }

    @task(2)
    def get_user(self):
        self.client.get(
            f"/user/{self.user_id}",
            headers=self.headers
        )

    @task(2)
    def get_watchlist(self):
        self.client.get(
            f"/user/{self.user_id}/watchlist",
            headers=self.headers
        )

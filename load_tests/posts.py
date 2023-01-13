import os

from locust import HttpUser, task, between
import json

username = os.getenv('GHOST_ADMIN_USERNAME')
password = os.getenv('GHOST_ADMIN_PASSWORD')


class GhostAPIUser(HttpUser):
    wait_time = between(1.0, 5.0)

    def on_start(self):
        data = {
            'username': username,
            'password': password
        }
        headers = {'Content-Type': 'application/json'}

        with self.client.post('/admin/session/', json=data, headers=headers, catch_response=True) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.fail()

    @task
    def get_posts(self):
        self.client.get('/admin/posts')

    @task
    def create_post(self):
        data = {
            'posts': [{
                'title': 'My Test Post',
                "mobiledoc": "{\"version\":\"0.3.1\",\"atoms\":[],\"cards\":[],\"markups\":[],\"sections\":[[1,\"p\","
                             "[[0,[],0,\"My post content. Work in progress...\"]]]]}",
                'status': 'published'
            }]
        }
        headers = {'Content-Type': 'application/json'}

        with self.client.post('/admin/posts', json=data, headers=headers, catch_response=True) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.fail()

        post_id = json.loads(response.text)['posts'][0]['id']
        self.get_post(post_id)

    def get_post(self, post_id):
        with self.client.get(f'/admin/posts/{post_id}', name="/ghost/api/admin/posts/$POST_ID", catch_response=True) as response:
            if response.status_code == 200 and json.loads(response.text)['posts'][0]['title'] == 'My Test Post':
                response.success()
            else:
                response.fail()

        self.delete_post(post_id)

    def delete_post(self, post_id):
        with self.client.delete(f'/admin/posts/{post_id}', name="/ghost/api/admin/posts/$POST_ID", catch_response=True) as response:
            if response.status_code == 204:
                response.success()
            else:
                response.fail()

        self.get_deleted_post(post_id)

    def get_deleted_post(self, post_id):
        with self.client.get(f'/admin/posts/{post_id}', name="/ghost/api/admin/posts/$POST_ID (not found)", catch_response=True) as response:
            if response.status_code == 404:
                response.success()
            else:
                response.fail()

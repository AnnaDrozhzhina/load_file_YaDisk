import requests

TOKEN = 'y0A'


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth{self.token}'
        }
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url=link_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, file_name):
        data = self._get_upload_link(disk_file_path=disk_file_path)
        url = data.get('href')
        response = requests.put(url=url, data=open(file_name, 'rb'))
        if response.status_code == 201:
            print('Success!')


if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk('test_17_04.txt', 'test.txt')
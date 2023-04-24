import requests


class YandexDisk:
    def __init__(self, token: str):
        self.token = token

    def _upload_file_to_disk(self, disk_file_path):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url=link_url, headers=headers, params=params).json()
        url = response.get('href','')
        response = requests.put(url=url, data=open(disk_file_path, 'rb'))
        if response.status_code == 201:
            print('Success!')


if __name__ == '__main__':
    TOKEN = 'y0'
    ya = YandexDisk(token=TOKEN)
    result = ya._upload_file_to_disk('test.txt')

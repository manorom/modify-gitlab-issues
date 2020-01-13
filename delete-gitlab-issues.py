import requests

gitlab_domain = 'Your Gitlab Domain.xyz'
headers = { 'PRIVATE-TOKEN': '<YOUR PRIVATE TOKEN>' }
project_id = 0
issues_range = range(0, 0)

def main():
    for issue_id in issues_range:
        url = f'https://{gitlab_domain}/api/v4/projects/{project_id}/issues/{issue_id}'
        print(requests.delete(url, headers=headers))

if __name__ == '__main__':
    main()

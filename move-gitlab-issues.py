import requests

headers = { 'PRIVATE-TOKEN': '<YOUR TOKEN>' }
github_domain = 'YOUR-GITLAB-DOMAIN'
old_project_id = 0 # YOUR OLD PROJECT ID
new_project_id = 0 # YOUR NEW PROJECT ID
all_issue_ids = range(0, 0)

def main():
    url = 'https://{github_domain}/api/v4/projects/{project_id}/issues/{issue_id}/move'
    form_data = {'to_project_id': new_project_id}

    for issue_id in all_issue_ids:
        url_with_params = url.format(github_domain=github_domain, project_id=old_project_id, issue_id=issue_id)
        resp = requests.post(url_with_params, headers=headers, data=form_data)
        if resp.status_code != 201:
            print(f'#{issue_id}: Failed with response {resp.status_code} {resp.json()}')
            return
        else:
            print(f'#{issue_id} ok {resp.status_code}')
main()

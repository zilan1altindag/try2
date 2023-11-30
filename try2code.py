import requests

def main():
    # Replace with the actual server address
    server_address = ' http://10.0.0.6/ctf_deploy/aclive/ddjS7HkE9M/A.php'

    # Replace with the correct combination of parameters
    params = {
        'osa': True,
        'osb': False,
        'osc': False,
        'xdqp': False,
        'awvp': False,
        'niqn': False,
        'wigq': False,
        'gusq': True,
        'rtoy': False
    }

    response = requests.get(server_address + '/policy/evaluate', params=params)

    if response.status_code == 200:
        print('Policy evaluated to true:')
        print('Flag:', response.json()['flag'])
    else:
        print('Error evaluating policy:', response.status_code)

if __name__ == '__main__':
    main()


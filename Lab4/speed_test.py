import requests
import time

def main():
    url = 'https://www.grsu.by/'
    start_time = time.time() 

    for i in range(20):
        try:
            response = requests.get(url)
            print(f'Request {i + 1}: Status {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Request {i + 1} failed: {e}')

    end_time = time.time()  
    total_time = end_time - start_time  
    print(f'Total time for 20 requests: {total_time:.2f} seconds')

if __name__ == '__main__':
    main()
import requests
from urllib.parse import quote_plus
from tqdm import tqdm
import time
import json

# 设置重试策略
retry_strategy = requests.packages.urllib3.util.retry.Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"]
)
adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)

def get_commits(owner, repo, headers, per_page=100, max_pages=100):
    all_commits = []
    for page in tqdm(range(1, max_pages + 1), desc="Fetching commits"):
        url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page={per_page}&page={page}"
        try:
            response = session.get(url, headers=headers)
            response.raise_for_status()

            if not response.text.strip():
                print(f"Empty response received for {owner}/{repo} on page {page}")
                continue

            commits = response.json()
            if not commits:
                break  # 如果没有更多提交，则退出循环

            all_commits.extend(commits)

            # 检查是否达到速率限制
            remaining = int(response.headers.get('X-RateLimit-Remaining', -1))
            if remaining <= 1:
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))
                wait_time = reset_time - time.time() + 10  # 加10秒缓冲时间
                print(f"Rate limit reached. Waiting for {wait_time:.0f} seconds...")
                time.sleep(wait_time)

            time.sleep(0.7)  # 避免触发API限速

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch commits for {owner}/{repo} on page {page}: {e}")
            continue
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON for {owner}/{repo} on page {page}: {e}")
            print(f"Response content: {response.text[:100]}...")  # 打印部分响应内容用于调试
            continue

    return all_commits


if __name__ == '__main__':
    owner = "torvalds"
    repo = "linux"
    headers = {
        'Authorization': 'token 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', 
        'Accept': 'application/vnd.github.v3+json'
    }

    commits = get_commits(owner, repo, headers)

    with open('LinuxCommitsInfo.txt', 'w',encoding='utf-8') as f:
        for commit in tqdm(commits, desc="Writing commits to file"):
            sha = commit['sha']
            message = commit['commit']['message']
            author = commit['commit']['author']['name']
            date = commit['commit']['author']['date']

            print(f"Commit SHA: {sha}\nMessage: {message}\nAuthor: {author}\nDate: {date}\n", file=f)
            print("-------------------------------------------\n",file=f)
    print(f"Total commits fetched: {len(commits)}")

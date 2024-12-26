from collections import defaultdict
import csv
def parse_info():
    categories = defaultdict(int)
    file_path = 'info.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        #分段
        commits = content.split('-------------------------------------------')
        #每一次commit进行提取
        for commit in commits:
            if not commit.strip():
                continue  # Skip empty entries

            lines = commit.strip().split('\n')

            for line in lines:
                if line.startswith('Message:'):
                    message = line[len('Message:'):].strip()

                    #merge tag xxx
                    if message.startswith('Merge tag'):
                        # Format 1
                        tag = message.split("'")[1]
                        categories[tag] += 1
                    #没有:
                    elif ':' not in message:
                        version = message
                        categories[version] += 1
                    #至少1个:
                    else:
                        parts = message.split(':', 2)
                        if message.count(':') == 1:
                            category = parts[0]
                        else:
                            category = parts[0]+ ':' + parts[1]
                        categories[category] += 1
                    break

    return dict(categories)

categories_count = parse_info()

def write_to_csv(categories_count, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Category', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for category, count in categories_count.items():
            writer.writerow({'Category': category, 'Count': count})

categories_count = parse_info()
output_file = 'category_counts.csv'
write_to_csv(categories_count, output_file)

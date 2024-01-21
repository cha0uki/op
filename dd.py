import csv
import os
import requests

# Open the results.csv file outside the loop
with open('results.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    with open('things.csv', 'r') as file:
        csv_reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Now, you can use a loop to iterate over each element in the row
            for element in row:
                # Process each element as needed

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + os.getenv('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',
                                           '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'),
                }

                json_data = {
                    'model': 'gpt-3.5-turbo',
                    'messages': [
                        {
                            'role': 'system',
                            'content': 'You are a helpful assistant.',
                        },
                        {
                            'role': 'user',
                            'content': f'Give me only the country {element} is from. Just the country in text, nothing else.',
                        },
                    ],
                }

                response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)

                # Check if the response status code is OK (200)
                if response.status_code == 200:
                    # Parse the JSON response
                    response_json = response.json()

                    # Extract and print the "content" from the response
                    content = response_json['choices'][0]['message']['content']

                    # Write both the element and the content to the results.csv file
                    print(content)
                    csv_writer.writerow([element, content])
                else:
                    print("Error:", response.status_code)

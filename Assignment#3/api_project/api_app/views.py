from django.shortcuts import render
import requests
import csv
# Create your views here.

def fetch_data(request):
    url = "https://api.publicapis.org/entries"  # Example public API
    response = requests.get(url)
    data = response.json()

    # Process JSON data and save to CSV
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for post in data:
            writer.writerow({'title': post['title'], 'body': post['body']})

            
    return render(request, 'data.html', {'data': data})

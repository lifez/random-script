import csv

occpuations = [
    'Bookkeeper',
    'Band director',
    'Architect',
    'Apartment manager',
    'Administrative assistant',
    'Administrative law judge',
    'Administrator',
    'Auditor',
    'Author',
    'Business professional',
]

templates = [
    'Funny Gag {OCCU} Coffee Mug - {QUOTE} - Best Perfect Gifts for {OCCU}',
    'Funny Gag {OCCU} Shot Glass - {QUOTE} - Best Perfect Gifts for {OCCU}',
    'Funny Gag {OCCU} Travel Coffee Mug - {QUOTE} - Best Perfect Gifts for {OCCU}'
]


with open('glass.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        results = []
        for occpuation in occpuations:
            print(row[0])
            if occpuation.upper() in row[0].upper():
                for template in templates:
                    result = template.replace('{OCCU}', occpuation).replace('{QUOTE}', row[0]).replace('{OCCU}', occpuation)
                    results.append(result)
        with open('output.csv', 'a') as f:
            writer = csv.writer(f)
            print(results)
            writer.writerows([results])

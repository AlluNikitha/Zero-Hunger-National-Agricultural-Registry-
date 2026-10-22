import os
import urllib.request
import pandas as pd

df = pd.read_csv('data/crop_data.csv')
if not os.path.exists('data/images'):
    os.makedirs('data/images')

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
urllib.request.install_opener(opener)

for idx, row in df.iterrows():
    url = row['Image_Url']
    if str(url).startswith('http'):
        url = url.replace('/thumb', '')
        url = url.rsplit('/', 1)[0]
        filename = f"data/images/crop_{row['Crop_ID']}.jpg"
        try:
            urllib.request.urlretrieve(url, filename)
            df.at[idx, 'Image_Url'] = filename
            print(f'Downloaded {filename}')
        except Exception as e:
            print(f'Failed {filename}: {e}')

df.to_csv('data/crop_data.csv', index=False)
print("Done!")

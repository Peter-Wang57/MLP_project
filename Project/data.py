import pandas as pd
import os
from sklearn.model_selection import train_test_split

current_path = os.getcwd()

test_data_path = os.path.join(current_path, 'test_data.txt')
row_dev_posts_path = os.path.join(current_path, 'posts.txt')
row_test_posts_path = os.path.join(current_path, 'posts_groundtruth.txt')
train_ekphrasis_path = os.path.join(current_path, 'train_ekphrasis.csv')
dev_ekphrasis_path = os.path.join(current_path, 'dev_ekphrasis.csv')
test_ekphrasis_path = os.path.join(current_path, 'test_ekphrasis.csv')

df = pd.read_table(row_dev_posts_path, sep='\t')
# df = pd.read_table(test_data_path, sep='\t')
df_test = pd.read_table(row_test_posts_path, sep='\t')

df = df.assign(cleaned_text=df['post_text'].copy())
df_test = df_test.assign(cleaned_text=df_test['post_text'].copy())

def map_label_to_enc_label(label):
    if label == 'fake':
        return 0
    elif label == 'real':
        return 1
    else:
        return None

df['enc_label'] = df['label'].apply(map_label_to_enc_label)
df_test['enc_label'] = df_test['label'].apply(map_label_to_enc_label)

df_train, df_dev = train_test_split(df, test_size=0.1)

print(df_train.info())
print("")
print(df_dev.info())
print("")
print(df_test.info())

df_train.to_csv(train_ekphrasis_path, index=False)
df_dev.to_csv(dev_ekphrasis_path, index=False)
df_test.to_csv(test_ekphrasis_path, index=False)
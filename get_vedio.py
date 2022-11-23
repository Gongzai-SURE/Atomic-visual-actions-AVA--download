import get_doc_path
import os
import urllib.request


def get_pic_by_url(folder_path, lists):
    if not os.path.exists(folder_path):
        print("Selected folder not exist, try to create it.")
        os.makedirs(folder_path)
    for url in lists:
        print("Try downloading file: {}".format(url))
        filename = url.split('/')[-1]
        filepath = folder_path + '/' + filename
        if os.path.exists(filepath):
            print("File have already exist. skip")
        else:
            try:
                urllib.request.urlretrieve(url, filename=filepath)
                print("Successfully download {}".format(url))
            except Exception as e:
                print("Error occurred when downloading file, error message:")
                print(e)


if __name__ == "__main__":
    root_path = 'D:\AVA\object_names'
    paths = get_doc_path.get_file(root_path)
    print(paths)

    for filename, path in paths.items():
        print('reading file: {}'.format(filename))

        with open(path, 'r') as f:
            lines = f.readlines()
            url_list = []
            for line in lines:
                url_list.append('http://s3.amazonaws.com/ava-dataset/'+os.path.splitext(filename)[0]+'/'+line.strip('\n'))
                print('https://s3.amazonaws.com/ava-dataset/'+os.path.splitext(filename)[0]+'/'+line.strip('\n'))

            foldername = "D:\AVA\{}".format(filename.split('.')[0])
            print(foldername)
            get_pic_by_url(foldername, url_list)
            print("{}数据集下载结束！".format(filename.split('.')[0]))



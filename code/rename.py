import os

def listdir_nohidden(path):
    nohidden = []
    for f in os.listdir(path):
        if not f.startswith('.'):
            nohidden.append(f)
    return nohidden

def rename_samples(filename):
    user_samples_path = os.path.join(samples_path, filename)

    print('rename filename: {}'.format(filename))

    user_samples = listdir_nohidden(user_samples_path)

    # testing
    # print('before sort')
    # for s in user_samples:
    #     print(s)
    # user_samples.sort(key=lambda x: os.path.getmtime(os.path.join(user_samples_path, x)))

    # print('*'*20)

    # print('after sort')
    # for s in user_samples:
    #     print(s)
    
    #  We can respecitively use `getmtime` or `getctime` to sort file by modified time or created time.
    user_samples.sort(key=lambda x: os.path.getmtime(os.path.join(user_samples_path, x)))   
    

    print('# of samples: {}'.format(len(user_samples)))

    for index, sample in enumerate(user_samples):
        os.rename(os.path.join(user_samples_path, sample), os.path.join(user_samples_path, ''.join([filename+'_'+str(index+1), '.png'])))


if __name__ == '__main__':
    main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(main_path, 'handwriting_dataset')
    croped_data_path = os.path.join(dataset_path, 'croped_data')
    samples_path = os.path.join(croped_data_path, 'samples')

    # filenames = listdir_nohidden(samples_path)
    filenames = ['test']
    print(filenames)

    for filename in filenames:
        rename_samples(filename)

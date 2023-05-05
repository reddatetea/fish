def shijiqijian(im_qijian0):

    if 'and' in im_qijian0:
        im_qijian0s = im_qijian0.strip().split('and')
        im_qijians = sorted(im_qijian0s)
        for im_qijian in im_qijians:
            print(im_qijian)
    else:
        im_qijians = im_qijian0.strip()

    print(im_qijians)
    return im_qijians


def main():
    im_qijian0 = '2020-03and2020-04 '
    im_qijians = shijiqijian(im_qijian0)
    if len(im_qijians) == 1 :
        im_qijian = im_qijians
    else :
        for im_qijian in im_qijians :
            print(im_qijian)

if __name__ == '__main__':
    main()




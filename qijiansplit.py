def shijiqijian(im_qijian0):
    im_qijians = []
    if 'and' in im_qijian0:
        im_qijian0s = im_qijian0.strip().split('and')
        im_qijian0s = sorted(im_qijian0s)

        for im_qijian in im_qijian0s:
            im_qijians.append(im_qijian)
    else:
        im_qijians.append(im_qijian0.strip())

    return im_qijians


def main():
    im_qijian0 = '2020-03'
    im_qijians = shijiqijian(im_qijian0)


if __name__ == '__main__':
    main()




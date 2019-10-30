import os
import shutil
import cv2

datasetROOT = '/media/smallflyfly/Data/Dataset/train/Person/'
# datasetROOT = '/Users/smallflyfly/Desktop/Dataset/train/Person/'
personTXT = './data/person_img.txt'
newDatasetpath = './Dataset/'
if not os.path.exists(newDatasetpath + 'images/'):
    os.mkdir(newDatasetpath + 'images/')

if not os.path.exists(newDatasetpath + 'labels/'):
    os.mkdir(newDatasetpath + 'labels/')

imgFils = os.listdir(datasetROOT + 'Images/')

print(len(imgFils))

iftxt = open(personTXT, 'wt')
for imgfile in imgFils:
    allfilename = datasetROOT + 'Images/' + imgfile
    filename = imgfile[:-4]
    iftxt.write(allfilename + '\n')
    # shutil.copy(allfilename, newDatasetpath+'images/')

    # img = cv2.imread(allfilename)
    # w, h = img.shape[1], img.shape[0]

    # labelfile = datasetROOT + 'Labels/' + filename + '.txt'  # class xmin ymin xmax ymax
    # txtfile = open(labelfile,'r')
    # lines = txtfile.readlines()
    # newLabelFile = open(newDatasetpath + 'labels/' + filename + '.txt', 'wt')
    # person = '0' #person class index 0
    # for line in lines:
    #     line = line.strip().split(' ')

    #     # print(line)
    #     # x1, y1, x2, y2 = int(float(line[1])), int(float(line[2])), int(float(line[3])), int(float(line[4]))
    #     # cv2.rectangle(img, (x1,y1), (x2, y2), (255, 0, 0), 1)
    #     # cv2.imshow('img',img)
    #     # cv2.waitKey()
    #     # cv2.destroyAllWindows()

    #     xmin = float(line[1])
    #     ymin = float(line[2])
    #     xmax = float(line[3])
    #     ymax = float(line[4])
    #     x_center_normalized = (xmin + xmax) / 2.0 / w
    #     y_center_normalized = (ymin + ymax) / 2.0 / h

    #     bbox_w_normalized = (xmax - xmin) / w
    #     bbox_h_normalized = (ymax - ymin) / h

    #     # print(x_center_normalized)
    #     # print(y_center_normalized)
    #     # print(bbox_w_normalized)
    #     # print(bbox_h_normalized)

    #     newLabelFile.write(person + ' ' + str(x_center_normalized) + ' ' + str(y_center_normalized) + ' ' + str(bbox_w_normalized) + ' ' + str(bbox_h_normalized) + '\n')
    # newLabelFile.close()
    # txtfile.close()

iftxt.close()
import os
import shutil
import cv2

datasetROOT = '/media/smallflyfly/Data/yolov3/Dataset/'
# datasetROOT = '/media/smallflyfly/Data/OIDv4_ToolKit-master/OID/Dataset/train/Car/'
# datasetROOT = 'G:\OIDv4_ToolKit-master\OID\Dataset\\train\Car\\'
# datasetROOT = '/Users/smallflyfly/Desktop/Dataset/train/Person/'
trainTXT = './data/trainCarPerson.txt'
# dataTXT = './data/carTrain.txt'
# newDatasetpath = './Dataset/Car/'
# if not os.path.exists(newDatasetpath + 'Images/'):
#     os.mkdir(newDatasetpath + 'Images/')

# if not os.path.exists(newDatasetpath + 'labels/'):
#     os.mkdir(newDatasetpath + 'labels/')

imgFils = os.listdir(datasetROOT+'images/')

# print(len(imgFils))

datatxt = open(trainTXT, 'wt')
count = 0
for imgfile in imgFils:
    allfilename = './Dataset/images/' + imgfile
    # filename = imgfile[:-4]
    datatxt.write(allfilename + '\n')
    # shutil.copy(allfilename, newDatasetpath+'images/')
    # print(allfilename)
    count += 1
    # print(str(count) + ' / ' + str(len(imgFils)))

    # img = cv2.imread(allfilename)
    # w, h = img.shape[1], img.shape[0]

    # labelfile = datasetROOT + 'Labels/' + filename + '.txt'  # class xmin ymin xmax ymax
    # # txtfile = open(labelfile,'r')
    # lines = txtfile.readlines()
    # newLabelFile = open(newDatasetpath + 'labels/' + filename + '.txt', 'wt')
    # car = '1' #person / car class index 0
    # for line in lines:
    #     line = line.strip().split(' ')

    #     x1, y1, x2, y2 = int(float(line[1])), int(float(line[2])), int(float(line[3])), int(float(line[4]))
    #     # cv2.rectangle(img, (x1,y1), (x2, y2), (255, 0, 0), 1)
    #     # cv2.imshow('img',img)
    #     # cv2.waitKey()
    #     # cv2.destroyAllWindows()

        # xmin = float(line[1])
        # ymin = float(line[2])
        # xmax = float(line[3])
        # ymax = float(line[4])
        # x_center_normalized = (xmin + xmax) / 2.0 / w
        # y_center_normalized = (ymin + ymax) / 2.0 / h

        # bbox_w_normalized = (xmax - xmin) / w
        # bbox_h_normalized = (ymax - ymin) / h

    #     # print(x_center_normalized)
    #     # print(y_center_normalized)
    #     # print(bbox_w_normalized)
    #     # print(bbox_h_normalized)

        # newLabelFile.write(car + ' ' + str(x_center_normalized) + ' ' + str(y_center_normalized) + ' ' + str(bbox_w_normalized) + ' ' + str(bbox_h_normalized) + '\n')
    # newLabelFile.close()
    # txtfile.close()
datatxt.close()
print(count)
print('Done!')
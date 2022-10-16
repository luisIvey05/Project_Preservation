import argparse
import glob
import sys
from utils.dataloader import preprocess


def main(train, data_path):
    if train == 0:
        TRAIN_BATCH_SIZE = 4
        VAL_BATCH_SIZE = 4
        train_list = glob.glob(data_path + '/train/*.txt')[0]
        val_list = glob.glob(data_path + '/val/*.txt')[0]

        trainloader, valloader = preprocess(data_path, TRAIN_BATCH_SIZE, VAL_BATCH_SIZE, train_list, val_list)









if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TRAINING MODULE FOR DEPTH ESTIMATION')
    parser.add_argument('--train', type=str, required=True, help="""'outdoor' OR 'indoor' """)
    parser.add_argument('--path', type=str, required=True, help='PATH TO DATASET')
    args = parser.parse_args()

    if args.train != 'outdoor' or args.train != 'indoor':
        sys.exit("User did not specify a correct option for --train")
    else:
        if args.train == 'outdoor':
            main(0, args.path)
        elif args.train == 'indoor':
            main(1, args.path)
import util
import cv2


def main():
    pass


if __name__ == "__main__":
    import argparse

    argument_parser = argparse.ArgumentParser("processing dataset for NN training")
    argument_parser.add_argument("-f", "--file_path", type=str, default=None, help="Directory of unprocessed finger images")
    argument_parser.add_argument("-d", "--debug_processing", default=False, action="store_true", help="Boolean to enable showing silhouetted folder")
    args = argument_parser.parse_args()

    if args.file_path is None or args.file_path == "":
        raise Exception("File path cannot be None or empty")
    args.show_silhouetting = args.debug_processing

    res = util.hand_silhouetting(None, args, args.file_path)

    while True:
        cv2.imshow("sillhouetted", res[0])
        cv2.imshow("cropped and sillhouetted", res[1])

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
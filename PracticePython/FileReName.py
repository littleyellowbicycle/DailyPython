import os


def Rename(path):
    if (os.path.isdir(path)):
        filelist = os.listdir(path)
        count = 1
        for file in filelist:
            os.rename(
                os.path.join(path, file),
                os.path.join(path, "image" + str(count) + ".jpg"))
            count += 1
    else:
        print("no find path ")
    pass


if __name__ == "__main__":
    Rename("D:\Games\World_of_Tanks\坦克世界外服高清壁纸\高清壁纸")
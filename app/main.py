import PyPDF2
from tools import get_file_list, change_dir, GetDesktopPath
import os
import shutil

# 文件构造方法，在tmp文件夹中进行相关文件处理，目前的逻辑为：遍历file_list文件，tmp中需要读取的pdf文件直接读取，如是压缩包，解压，并将文件名加入文件路径
def file_builder(file_list):
    pdfs = []
    path = "tmp\\"
    try:
        for i in file_list:
            name = i['name']
            file_name, extension_name = os.path.splitext(name)
            if extension_name == '.pdf':
                pdfs.append(path + name)
            elif extension_name == '.7z' | '.zip' | '.rar':
                print(file_name)
                continue
            else:
                continue
    except:
        print("error")
    return pdfs


def clean_files():
    if os.path.exists("combined_PDF.pdf"):
        os.remove("combined_PDF.pdf")
    if os.path.exists("tmp"):
        shutil.rmtree("tmp")
        os.mkdir("tmp")
    return True

# 这段是借鉴的，目前是把一张a4纸上面放两个pdf，具体程度待测试
def pdf_merge(pdfs, output):
    writer = PyPDF2.PdfFileWriter()
    for n, item in enumerate(pdfs):
        pageobj = PyPDF2.PdfFileReader(item).getPage(0)
        if n % 2 == 0:
            blankpage = writer.addBlankPage(610, 810)
            blankpage.mergeTranslatedPage(pageobj, 0, 410)
        else:
            blankpage.mergeTranslatedPage(pageobj, 0, 0)

    writer.removeLinks()  # 移除交互链接,部分发票pdf文件在位移后会有图章重复的情况,需要移除.
    writer.write(open(output, 'wb'))  # 写入新的文件,完成合并.

# def main():
#     desktop = GetDesktopPath()
#     dirs = str(desktop) + "\\"
#     pdfs = get_file_list(dirs)
#     # 合并完成的pdf名称
#     output = 'combined.pdf'
#     # 调用merge函数，进行合并
#     pdf_merge(pdfs, output)
#
#
# if __name__ == '__main__':
#     main()

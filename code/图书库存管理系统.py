# 图书库存管理系统
# 图书类
class book:
    def __init__(self,name,writer,pubyear):
        self.name=name
        self.writer=writer
        self.pubyear=pubyear

    def __str__(self):
        return f'书名:{self.name} | 作者:{self.writer} | 出版时间:{self.pubyear}'

    # 修改图书信息
    def update_book(self,name=None,writer=None,pubyear=None):
        if name is not None :
            self.name=name
        if writer is not None:
            self.writer=writer
        if pubyear is not None:
            self.pubyear=pubyear

# 图书库存管理系统类
class BookManagement():
    system_name='图书库存管理系统'
    system_version='1.0'

    # 创建列表,记录图书库存信息
    def __init__(self):
        self.book_list=[] # 列表,记录图书信息

    # 添加图书
    def add_book(self):
        name=input('请输入图书名称:')

        # 判断图书是否存在,如果存在,则添加失败(不能重复添加)
        for book in self.book_list:
            if book['name'] == name:
                print('该书已经存在,请重新添加')
                return

        writer=input('请输入作者名称:')
        pubyear =input('请输入图书出版时间:')
        print('图书信息添加成功~')

    # 修改图书信息
    def update_book(self):
        name = input('请输入图书名称:')

        # 根据图书名称找到该图书信息
        for book in self.book_list:
            if book['name'] == name:
                print(f'当前图书:{book}')

                writer = input('请输入修改后的作者名称:')
                pubyear = input('请输入修改后的图书出版时间:')
                print('图书信息修改成功~')
                return
        print('未找到该图书,修改失败!')

    # 删除图书信息
    def delete_book(self):
        name = input('请输入图书名称:')

        for book in self.book_list:
            if book['name'] == name:
                self.book_list.remove(book)
                print('图书信息删除成功~')
                return

        print('未找到该图书,删除失败!')

    # 查询指定图书信息
    def query_book(self):
        name = input('请输入图书名称:')

        for book in self.book_list:
            if book['name'] == name:
                print(f'图书信息:{book}')
                return
        print('未找到该图书!')
    # 展示全部图书信息
    def lisi_book(self):
        for book in self.book_list:
            print(book)
    # 运行系统
    def run(self):
        print(f'欢迎使用图书库存管理系统 V{BookManagement.system_version}')

        while True:
            print()
            print('#################################################################################')
            print('# 1.添加图书    2.修改图书   3.删除图书   4.查询指定图书    5.展示所有图书   6.退出系统 #')
            print('#################################################################################')
            print()
            choice=int(input('请选择要执行的操作,请输入1~6:'))

            try:
                match choice:
                    case 1: # 添加图书
                        self.add_book()
                    case 2: # 修改图书
                        self.update_book()
                    case 3: # 删除图书
                        self.delete_book()
                    case 4: # 查询指定图书
                        self.query_book()
                    case 5: # 展示所有图书
                        self.lisi_book()
                    case 6: # 退出系统
                        print('拜拜~')
                        break
                    case _: # 其他情况
                        print('输入错误,请选择1~6之间的菜单功能!')
            except Exception as e:
                print(e)
                print('程序运行出错了,请重新选择~')

# 运行
book_management=BookManagement()
book_management.run()

































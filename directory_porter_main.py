import os
import sys
import shutil
import ctypes
from PyQt5 import QtCore, QtWidgets
from directory_porter_ui import Ui_MainWindow


class Porter(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, window):
        self.__version__ = '0.1.0'
        self.__author__ = 'ZhZYX (i@zhzyx.me)'

        QtWidgets.QMainWindow.__init__(self, parent=None)

        debug = True  # 以管理员重启就无法被 debugger 追踪到了, 因此加一个选项
        if not ctypes.windll.shell32.IsUserAnAdmin() and not debug:  # 检查是不是管理员权限
            QtWidgets.QMessageBox.warning(self, '权限不足', '权限不足: 应用将重新以管理员权限启动.',
                                          QtWidgets.QMessageBox.Yes)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit()

        self.setupUi(window)  # 设置 UI
        self.connect_slots()

    def connect_slots(self):
        # 连接槽函数
        self.pushButton_selectSource.clicked.connect(
            self.on_pushButton_selectSource_clicked)
        self.pushButton_selectTarget.clicked.connect(
            self.on_pushButton_selectTarget_clicked)
        self.pushButton_execute.clicked.connect(
            self.on_pushButton_execute_clicked)

    @QtCore.pyqtSlot()
    def on_pushButton_selectSource_clicked(self):
        self.statusbar.showMessage('')
        source_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Source directory")
        if source_path:
            self.lineEdit_source.setText(source_path)

    @QtCore.pyqtSlot()
    def on_pushButton_selectTarget_clicked(self):
        self.statusbar.showMessage('')
        target_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Target directory")
        if target_path:
            self.lineEdit_target.setText(target_path)

    @QtCore.pyqtSlot()
    def on_pushButton_execute_clicked(self):
        self.set_widget_enable(False)
        self.execute_migration()
        self.set_widget_enable(True)

    def execute_migration(self):
        source_path = self.lineEdit_source.text()
        target_path = self.lineEdit_target.text()

        self.statusbar.showMessage('正在检查地址...')
        if not self.check_paths(source_path, target_path):
            return False

        raw_source_name = os.path.split(source_path)[1]
        temp_source_path = source_path + '.old'
        full_target_path = os.path.join(target_path + '/' + raw_source_name)

        self.statusbar.showMessage('正在重命名源文件夹...')
        if not self.rename_dir(source_path, temp_source_path):
            return False  # 重命名失败则中止

        self.statusbar.showMessage('正在复制到目标文件夹...')
        if not self.copy_dir(temp_source_path, full_target_path):
            self.rename_dir(temp_source_path, source_path)  # 复原名称
            return False

        self.statusbar.showMessage('正在建立符号链接...')
        if not self.make_link(source_path, full_target_path):
            self.rename_dir(temp_source_path, source_path)
            return False

        self.statusbar.showMessage('正在删除源文件...')
        if not self.remove_dir(temp_source_path):
            self.statusbar.showMessage('文件夹迁移成功, 但源文件未能成功删除.')
            return False

        # 此时所有流程都已结束, 在状态栏中提示成功
        self.statusbar.showMessage('文件夹迁移成功!')
        return True

    def remove_dir(self, dir_path):
        try:
            shutil.rmtree(dir_path)
        except Exception as e:
            self.warning('删除文件夹出错',
                         f'删除文件夹 "{dir_path}" 时发生错误: {str(e)}, 请手动移除或重新指定位置.')
            return False
        else:
            return True

    def make_link(self, source_path, full_target_path):
        if not os.path.isdir(full_target_path):
            self.warning('目标不是文件夹', f'"{full_target_path}" 不是文件夹.')
            return False

        try:
            os.symlink(full_target_path, source_path)
        except FileExistsError:
            self.warning('存在同名文件夹', f'目标文件夹下已存在同名对象: "{full_target_path}", 请手动移除.')
            print(os.path.split(full_target_path)[0])
            os.startfile(os.path.split(full_target_path)[0])
        except Exception as e:
            self.warning('未知错误', str(e))
        else:  # 没有异常发生
            return True
        return False  # 有异常发生

    def copy_dir(self, source_path, full_target_path):
        try:
            shutil.copytree(source_path, full_target_path)
        except FileExistsError:
            self.warning('存在同名文件夹', f'目标文件夹下已存在同名对象: "{full_target_path}", 请手动移除.')
            os.startfile(os.path.split(full_target_path)[0])
        except Exception as e:
            self.warning('未知错误', str(e))
        else:  # 没有异常发生
            return True
        return False  # 有异常发生

    def set_widget_enable(self, flag=True):
        self.lineEdit_target.setEnabled(flag)
        self.lineEdit_source.setEnabled(flag)
        self.pushButton_execute.setEnabled(flag)
        self.pushButton_selectTarget.setEnabled(flag)
        self.pushButton_selectSource.setEnabled(flag)

    def check_paths(self, source_path, target_path):
        def check_dir(dir_path):
            if not os.path.isdir(dir_path):
                self.warning('文件夹检查错误', f'目标: "{dir_path}" 不存在或者不是文件夹.')
                return False
            return True

        if not (check_dir(source_path) and check_dir(target_path)):
            return False  # 目标不存在或者不是文件夹则中止
        if source_path == target_path:
            self.warning('路径错误', f'源文件夹 "{source_path}" 和目标文件夹 "{target_path}" 不能相同!')
            return False  # 两个文件夹不能相同
        if os.path.split(source_path)[0] == target_path:
            self.warning('路径错误', f'源文件夹 "{source_path}" 不能是目标文件夹 "{target_path}" 的子文件夹!')
            return False  # 源文件夹不能是目标文件夹的子文件夹
        return True

    def rename_dir(self, src, dst):
        if src and dst:  # 两者同时存在
            try:
                os.rename(src, dst)
            except FileNotFoundError:
                self.warning('重命名失败', f'找不到目标: "{src}"')
            except FileExistsError:
                self.warning('重命名失败', f'目标: "{dst}" 已存在!')
            except Exception as e:
                self.warning('未知错误', str(e))
            else:  # 如果没有异常发生
                return True
        else:
            self.warning('重命名失败', f'找不到指定的路径: "{src}" -> "{dst}"')

        return False  # 有异常发生, 也就是没有在 try else 部分返回

    def warning(self, title, msg):
        QtWidgets.QMessageBox.warning(self, title, msg, QtWidgets.QMessageBox.Ok)
        self.statusbar.showMessage(title)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Porter(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

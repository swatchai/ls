# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_settings.ui'
#
# Created: Fri Jan 09 14:23:20 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PluginSettingsDialog(object):
    def setupUi(self, PluginSettingsDialog):
        PluginSettingsDialog.setObjectName(_fromUtf8("PluginSettingsDialog"))
        PluginSettingsDialog.resize(388, 203)
        self.SettingsTab = QtGui.QTabWidget(PluginSettingsDialog)
        self.SettingsTab.setGeometry(QtCore.QRect(10, 10, 371, 151))
        self.SettingsTab.setObjectName(_fromUtf8("SettingsTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.HomeDirEdit = QtGui.QLineEdit(self.tab)
        self.HomeDirEdit.setGeometry(QtCore.QRect(10, 30, 321, 20))
        self.HomeDirEdit.setObjectName(_fromUtf8("HomeDirEdit"))
        self.LogDirLabel = QtGui.QLabel(self.tab)
        self.LogDirLabel.setGeometry(QtCore.QRect(10, 60, 351, 21))
        self.LogDirLabel.setObjectName(_fromUtf8("LogDirLabel"))
        self.HomeDirLabel = QtGui.QLabel(self.tab)
        self.HomeDirLabel.setGeometry(QtCore.QRect(10, 10, 351, 21))
        self.HomeDirLabel.setObjectName(_fromUtf8("HomeDirLabel"))
        self.LogDirButton = QtGui.QPushButton(self.tab)
        self.LogDirButton.setGeometry(QtCore.QRect(330, 80, 31, 23))
        self.LogDirButton.setObjectName(_fromUtf8("LogDirButton"))
        self.HomeDirButton = QtGui.QPushButton(self.tab)
        self.HomeDirButton.setGeometry(QtCore.QRect(330, 30, 31, 23))
        self.HomeDirButton.setObjectName(_fromUtf8("HomeDirButton"))
        self.LogDirEdit = QtGui.QLineEdit(self.tab)
        self.LogDirEdit.setGeometry(QtCore.QRect(10, 80, 321, 20))
        self.LogDirEdit.setObjectName(_fromUtf8("LogDirEdit"))
        self.SettingsTab.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.FontLabel = QtGui.QLabel(self.tab_3)
        self.FontLabel.setGeometry(QtCore.QRect(10, 10, 351, 41))
        self.FontLabel.setScaledContents(False)
        self.FontLabel.setWordWrap(True)
        self.FontLabel.setObjectName(_fromUtf8("FontLabel"))
        self.FontNameLabel = QtGui.QLabel(self.tab_3)
        self.FontNameLabel.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.FontNameLabel.setObjectName(_fromUtf8("FontNameLabel"))
        self.FontNameCombo = QtGui.QFontComboBox(self.tab_3)
        self.FontNameCombo.setGeometry(QtCore.QRect(90, 60, 156, 21))
        self.FontNameCombo.setObjectName(_fromUtf8("FontNameCombo"))
        self.FontSizeLabel = QtGui.QLabel(self.tab_3)
        self.FontSizeLabel.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.FontSizeLabel.setObjectName(_fromUtf8("FontSizeLabel"))
        self.FontSizeCombo = QtGui.QComboBox(self.tab_3)
        self.FontSizeCombo.setGeometry(QtCore.QRect(90, 90, 41, 22))
        self.FontSizeCombo.setObjectName(_fromUtf8("FontSizeCombo"))
        self.SettingsTab.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.LineToleranceLabel = QtGui.QLabel(self.tab_2)
        self.LineToleranceLabel.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.LineToleranceLabel.setObjectName(_fromUtf8("LineToleranceLabel"))
        self.LineToleranceEdit = QtGui.QLineEdit(self.tab_2)
        self.LineToleranceEdit.setGeometry(QtCore.QRect(140, 10, 121, 20))
        self.LineToleranceEdit.setObjectName(_fromUtf8("LineToleranceEdit"))
        self.AreaToleranceLabel = QtGui.QLabel(self.tab_2)
        self.AreaToleranceLabel.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.AreaToleranceLabel.setObjectName(_fromUtf8("AreaToleranceLabel"))
        self.AreaToleranceEdit = QtGui.QLineEdit(self.tab_2)
        self.AreaToleranceEdit.setGeometry(QtCore.QRect(140, 40, 121, 20))
        self.AreaToleranceEdit.setObjectName(_fromUtf8("AreaToleranceEdit"))
        self.MaxIterationLabel = QtGui.QLabel(self.tab_2)
        self.MaxIterationLabel.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.MaxIterationLabel.setObjectName(_fromUtf8("MaxIterationLabel"))
        self.MaxIterationEdit = QtGui.QLineEdit(self.tab_2)
        self.MaxIterationEdit.setGeometry(QtCore.QRect(140, 70, 121, 20))
        self.MaxIterationEdit.setObjectName(_fromUtf8("MaxIterationEdit"))
        self.SettingsTab.addTab(self.tab_2, _fromUtf8(""))
        self.OKButton = QtGui.QPushButton(PluginSettingsDialog)
        self.OKButton.setGeometry(QtCore.QRect(190, 170, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OKButton.sizePolicy().hasHeightForWidth())
        self.OKButton.setSizePolicy(sizePolicy)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.CancelButton = QtGui.QPushButton(PluginSettingsDialog)
        self.CancelButton.setGeometry(QtCore.QRect(290, 170, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(PluginSettingsDialog)
        self.SettingsTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(PluginSettingsDialog)

    def retranslateUi(self, PluginSettingsDialog):
        PluginSettingsDialog.setWindowTitle(_translate("PluginSettingsDialog", "Plugin Settings", None))
        self.HomeDirEdit.setToolTip(_translate("PluginSettingsDialog", "Default directory for loading fieldbooks.", None))
        self.LogDirLabel.setToolTip(_translate("PluginSettingsDialog", "Directory for log file.", None))
        self.LogDirLabel.setText(_translate("PluginSettingsDialog", "Log directory:", None))
        self.HomeDirLabel.setToolTip(_translate("PluginSettingsDialog", "Default directory for loading fieldbooks.", None))
        self.HomeDirLabel.setText(_translate("PluginSettingsDialog", "Home directory:", None))
        self.LogDirButton.setText(_translate("PluginSettingsDialog", "...", None))
        self.HomeDirButton.setText(_translate("PluginSettingsDialog", "...", None))
        self.LogDirEdit.setToolTip(_translate("PluginSettingsDialog", "Directory for log file.", None))
        self.SettingsTab.setTabText(self.SettingsTab.indexOf(self.tab), _translate("PluginSettingsDialog", "Directories", None))
        self.FontLabel.setText(_translate("PluginSettingsDialog", "Monospace font used in the calculation results widgets on Linux. On Windows it is courier font.", None))
        self.FontNameLabel.setText(_translate("PluginSettingsDialog", "Font name:", None))
        self.FontSizeLabel.setText(_translate("PluginSettingsDialog", "Font size:", None))
        self.SettingsTab.setTabText(self.SettingsTab.indexOf(self.tab_3), _translate("PluginSettingsDialog", "Font", None))
        self.LineToleranceLabel.setText(_translate("PluginSettingsDialog", "Snap tolerance:", None))
        self.AreaToleranceLabel.setText(_translate("PluginSettingsDialog", "Area tolerance:", None))
        self.MaxIterationLabel.setText(_translate("PluginSettingsDialog", "Max. iterations:", None))
        self.SettingsTab.setTabText(self.SettingsTab.indexOf(self.tab_2), _translate("PluginSettingsDialog", "Area division", None))
        self.OKButton.setText(_translate("PluginSettingsDialog", "OK", None))
        self.CancelButton.setText(_translate("PluginSettingsDialog", "Cancel", None))

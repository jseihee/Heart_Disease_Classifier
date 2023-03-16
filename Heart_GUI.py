from PyQt6 import QtWidgets, uic
import pandas as pd
import numpy as np
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QMessageBox
from ML import ML


def readData():
    age = call.lineEdit_Age.text()
    sex = call.comboBox_Sex.currentIndex()
    CP = call.comboBox_CP.currentIndex()
    BP = call.lineEdit_BP.text()
    chol = call.lineEdit_Chol.text()
    FBS = call.comboBox_FBS.currentIndex()
    ECG = call.comboBox_ECG.currentIndex()
    HR = call.lineEdit_HR.text()
    EIA = call.comboBox_EIA.currentIndex()
    STD = call.lineEdit_STP.text()
    STS = call.comboBox_STS.currentIndex()
    CMBV = call.comboBox_CMBV.currentIndex()
    thal = call.comboBox_Thal.currentIndex()

    data = [age, sex, CP, BP, chol, FBS, ECG, HR, EIA, STD, STS, CMBV, thal]
    for i in range(len(data)):
        if data[i] == -1 or data[i] == "":
            data[i] = np.nan
    return createDf(data)


def confirmClear():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Question)
    msg.setText(f"Are you are you wish to clear the data?")
    msg.setWindowTitle("Confirm")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    result = msg.exec()
    if result == QMessageBox.StandardButton.Ok:
        clearData()


def confirmSubmit():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Question)
    msg.setText(f"Are you are you wish to submit the data?")
    msg.setWindowTitle("Confirm")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    result = msg.exec()
    if result == QMessageBox.StandardButton.Ok:
        readData()


def createDf(data):
    userDF = pd.DataFrame([data], columns=['Age', 'Sex', 'Chest_pain_type', 'Resting_bp',
                                           'Cholesterol', 'Fasting_bs', 'Resting_ecg',
                                           'Max_heart_rate', 'Exercise_induced_angina',
                                           'ST_depression', 'ST_slope', 'Num_major_vessels',
                                           'Thallium_test'])
    result = ML(userDF)
    result = "Positive" if result[0] == 1 else "Negative"
    return showResults(result)


def showResults(result):
    msg = QMessageBox()
    msg.setText(f"Result: {result}")
    msg.setWindowTitle("Results")
    msg.exec()


def clearData():
    call.lineEdit_Age.clear()
    call.comboBox_Sex.setCurrentIndex(-1)
    call.comboBox_CP.setCurrentIndex(-1)
    call.lineEdit_BP.clear()
    call.lineEdit_Chol.clear()
    call.comboBox_FBS.setCurrentIndex(-1)
    call.comboBox_ECG.setCurrentIndex(-1)
    call.lineEdit_HR.clear()
    call.comboBox_EIA.setCurrentIndex(-1)
    call.lineEdit_STP.clear()
    call.comboBox_STS.setCurrentIndex(-1)
    call.comboBox_CMBV.setCurrentIndex(-1)
    call.comboBox_Thal.setCurrentIndex(-1)


app = QtWidgets.QApplication([])
call = uic.loadUi("UI_Design.ui")

validator = QRegularExpressionValidator(QRegularExpression(r'[0-9]+'))
decimalValidator = QRegularExpressionValidator(QRegularExpression(r'[0-9]+\.[0-9]'))
call.lineEdit_HR.setValidator(validator)
call.lineEdit_STP.setValidator(decimalValidator)
call.lineEdit_BP.setValidator(validator)
call.lineEdit_Age.setValidator(validator)
call.lineEdit_Chol.setValidator(validator)

call.pushButton.clicked.connect(confirmSubmit)
call.pushButton_2.clicked.connect(confirmClear)

call.show()
app.exec()

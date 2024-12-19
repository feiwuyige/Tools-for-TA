# Tools-for-TA
## 1. 批量解压压缩包（unzip.py）
解压rar文件的时候，由于格式问题，可能会导致出现 `Not a RAR file` 的错误，此时手动解压。同时由于 `rarfile` 库需要 `rar` 以及 `unrar` 的支持，请确保安装了 **RAR** 解压工具并正确配置了环境变量。

## 2. 统计作业提交情况(submission.py)
作业提交的命名格式为：姓名+学号，其中学号长度为12位，利用学号作为关键字，在excel表格中进行查找，对于已经提交作业的同学置为1，否则置为0，并将单元格置为黄色。

## 3. 统计学习实验整理(filecopy.ps1)
统计学习提交的实验很多人都是文件夹乱放，但是主要评分依据 "regression_test.csv", "svm_classification_test.csv","mlp_classfication_test.csv","adaboost_classification_test.csv"。所以该函数的主要目的是去遍历文件夹中的所有文件，将符合要求的文件复制一份至其他文件，然后方便统一处理。
注意文件路径中不要出现中文，不然由于编码问题会出现错误。
在后续评分的时候，发现有些人的文件里面有多个同名文件，之前的逻辑会进行覆盖，这部分人手动处理。

## 4. 根据标准答案进行评分(score.py)
对于回归，与标准答案计算mse；对于分类问题，与标准答案计算accuracy。

## 5. 汇总excel表格并算平均分

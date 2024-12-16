function Copy-File {
    param (
        [string]$fileName  # 需要复制的文件名称
    )

    # 固定的源文件夹路径
    $sourceFolder = "your_path"   # 请替换为源文件夹路径

    # 固定的目标文件夹路径
    $destinationFolder = "your_path"  # 请替换为目标文件夹路径

    # 遍历源文件夹中的所有子文件夹（包括多层深的子文件夹）
    # Get-ChildItem -Recurse 获取当前目录下的所有文件和文件夹 
    # Where-Object 用于过滤，只选择文件名为fileName的文件
    $sourceFiles = Get-ChildItem -Path $sourceFolder -Recurse | Where-Object { $_.Name -eq $fileName }

    # 如果找到匹配的文件，进行复制
    foreach ($sourceFile in $sourceFiles) {
        # 获取文件的第一层子文件夹名称
        # sourceFile.DirectoryName返回文件所在的文件夹
        # substring 方法得到去掉源文件夹路径后的字符串，TrimStart去掉开头的反斜杠
        $relativePath = $sourceFile.DirectoryName.Substring($sourceFolder.Length).TrimStart("\")
        $firstLevelFolder = $relativePath.Split('\')[0]  # 获取第一层文件夹的名称

        # 在目标文件夹中创建相应的第一层子文件夹
        $targetFolder = Join-Path -Path $destinationFolder -ChildPath $firstLevelFolder
        if (-not (Test-Path $targetFolder)) {
            New-Item -Path $targetFolder -ItemType Directory
        }

        # 将文件复制到目标文件夹
        $destFile = Join-Path -Path $targetFolder -ChildPath $fileName
        Copy-Item $sourceFile.FullName -Destination $destFile -Force
        <# Write-Host "from $($sourceFile.FullName) to $destFile" #>
    }
}

# 调用函数复制文件
Copy-File -fileName "regression_test.csv"
Copy-File -fileName "svm_classification_test.csv"
Copy-File -fileName "mlp_classification_test.csv"
Copy-File -fileName "adaboost_classification_test.csv"
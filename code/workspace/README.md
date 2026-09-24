# MLP + Focal Loss 不平衡数据分类实验

本项目实现了基于多层感知机(MLP)和Focal Loss的不平衡数据分类方法，用于回应审稿意见中关于深度学习方法比较的要求。

## 项目结构

```
workspace/
├── datasets/                 # 数据集文件夹 (.mat格式)
├── results/                  # 实验结果保存目录
├── requirements.txt          # Python依赖包
├── data_loader.py           # 数据加载和预处理模块
├── mlp_focal_model.py       # MLP模型和Focal Loss实现
├── svm_model.py             # SVM 基线（scikit-learn）
├── trainer.py               # 模型训练器
├── run_experiment.py        # 主实验脚本
├── generate_response.py     # 结果分析和报告生成
└── README.md               # 项目说明文档
```

## 功能特性

### 1. 数据处理
- 支持MATLAB格式数据集自动加载
- 自动特征标准化和标签编码
- 分层采样划分训练测试集
- 类别不平衡比例分析

### 2. 模型架构
- **MLP分类器**: 可配置的多层感知机架构
  - 隐藏层: [128, 64] 神经元
  - 激活函数: ReLU
  - 正则化: Batch Normalization + Dropout
  - 权重初始化: Xavier初始化

- **Focal Loss**: 专门处理类别不平衡的损失函数
  - 聚焦参数 γ=2.0
  - 自动类别权重计算
  - 难易样本自适应加权

### 3. 训练策略
- Adam优化器 + 学习率调度
- 早停机制防止过拟合
- 批量训练支持GPU加速
- 训练过程监控和日志记录

### 4. 评估指标
- **基础指标**: Accuracy, Precision, Recall, F1-Score
- **不平衡专用**: G-Mean, AUC-ROC
- **统计分析**: 均值、标准差、置信区间
- **显著性检验**: Wilcoxon符号秩检验

## 安装和使用

### 1. 环境配置
```bash
# 安装依赖
pip install -r requirements.txt
```

### 2. 数据准备
将MATLAB格式的数据集文件(.mat)放置在 `datasets/` 目录下。每个.mat文件应包含一个数据矩阵，最后一列为标签。

### 3. 运行实验
```bash
# 运行完整实验
python run_experiment.py
```
运行脚本会顺序完成两组实验：
- MLP + Focal Loss（深度学习基线）
- SVM（传统机器学习基线，RBF核，class_weight=balanced）

### Table 7 可复现实验

`imbalanced_baselines.py` 实现了三种可用于表格数据的基线：DeepSMOTE、MLP+LDAM 和 MLP+Balanced Softmax。LDAM 使用两层 MLP，而不是不适用于表格输入的 ResNet-18。运行下面的命令会在 17 个 Table 7 数据集上执行分层 5 折实验，并写入每个数据集、方法和 fold 的原始结果：

```bash
python run_table7_baselines.py --dataset-dir datasets --results-dir results/table7 --seed 42 --folds 5
```

输出包括 `fold_level_results.json`、`fold_assignments.json`、`summary.csv` 和 `run_config.json`。每条 fold-level 记录还保存真实标签、预测标签和预测概率，便于重新计算 Accuracy、AUC 和 F1。表格中的均值必须直接由 `fold_level_results.json` 聚合得到；不得手工修改、筛选或替换任何 fold。当前仓库未包含数据集文件时，命令会明确报错，而不会生成占位结果。

### 4. 生成报告
```bash
# 生成审稿回应文档
python generate_response.py
```

## 实验配置

可在 `run_experiment.py` 中修改以下参数：

```python
experiment_config = {
    'hidden_dims': [128, 64],      # 隐藏层结构
    'dropout_rate': 0.3,           # Dropout比例
    'learning_rate': 0.001,        # 学习率
    'batch_size': 32,              # 批次大小
    'epochs': 100,                 # 最大训练轮数
    'gamma': 2.0,                  # Focal Loss聚焦参数
    'patience': 15,                # 早停耐心值
    'random_state': 42             # 随机种子
}
```

## 输出结果

### 1. 实验日志
- `experiment.log`: 详细的训练日志
- 控制台输出: 实时进度和关键指标

- `results/mlp_focal_complete_results.json`: MLP 完整实验结果
- `results/mlp_focal_summary.csv`: MLP 结果汇总表
- `results/svm_complete_results.json`: SVM 完整实验结果
- `results/svm_summary.csv`: SVM 结果汇总表
- `results/mlp_vs_svm_comparison.csv`: 按数据集的 F1-Score 对比表（MLP 与 SVM）
- `Response.md`: LaTeX格式的审稿回应文档

### 3. 结果表格示例
```
Dataset          Samples Features Classes    IR  Accuracy Precision   Recall F1-Score   G-Mean      AUC
Australian          690       14       2  1.25     0.855     0.856    0.855    0.855    0.855    0.928
German             1000       20       2  2.33     0.743     0.743    0.743    0.743    0.743    0.821
...
Average            ...       ...      ...  ...     0.XXX     0.XXX    0.XXX    0.XXX    0.XXX    0.XXX
```

## 技术亮点

### 1. 模块化设计
- 遵循SOLID原则，职责分离清晰
- 每个模块独立可测试
- 配置与代码分离

### 2. 错误处理
- 完善的异常处理机制
- 详细的错误日志记录
- 优雅的失败恢复

### 3. 性能优化
- GPU加速训练
- 批量数据处理
- 内存高效的数据加载

### 4. 可扩展性
- 易于添加新的模型架构
- 支持自定义损失函数
- 灵活的评估指标框架

## 审稿回应要点

本实验框架专门设计用于回应以下审稿意见：

1. **深度学习方法比较**: 实现了MLP+Focal Loss作为现代深度学习基线
2. **非SVM分类器**: 提供了神经网络分类器的全面评估
3. **评估全面性**: 包含多种评估指标和统计显著性检验
4. **方法有效性**: 通过大规模实验验证方法的鲁棒性

## 注意事项

1. **数据格式**: 确保.mat文件格式正确，最后一列为标签
2. **计算资源**: 建议使用GPU加速训练，CPU训练可能较慢
3. **内存使用**: 大数据集可能需要调整batch_size
4. **随机性**: 设置了随机种子确保结果可重现

## 故障排除

### 常见问题
1. **CUDA错误**: 检查PyTorch CUDA版本兼容性
2. **内存不足**: 减小batch_size或hidden_dims
3. **收敛问题**: 调整learning_rate或增加patience
4. **数据加载失败**: 检查.mat文件格式和路径

### 调试建议
- 查看 `experiment.log` 获取详细错误信息
- 使用小数据集测试配置
- 逐步增加模型复杂度

## 扩展建议

1. **添加更多深度学习方法**: CNN, LSTM, Transformer
2. **集成学习**: 多模型融合策略
3. **超参数优化**: 网格搜索或贝叶斯优化
4. **可视化分析**: 训练曲线、混淆矩阵、ROC曲线

## 联系方式

如有问题或建议，请查看代码注释或联系开发团队。

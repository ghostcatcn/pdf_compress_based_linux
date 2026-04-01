# PDF 压缩工具使用说明

## 工具简介

这是一个基于 Python 和 Ghostscript 的 PDF 文件压缩工具，可在 Linux 系统上使用。它提供了三种压缩质量级别，能够有效减小 PDF 文件的大小，同时保持合理的视觉质量。

### 功能特点
- 支持三种压缩质量级别：低（最大压缩）、中（默认）、高（最小压缩）
- 自动计算压缩前后的文件大小和压缩率
- 提供友好的命令行界面
- 操作简单，易于集成到其他工作流程中
- **大文件优化**：支持处理数百MB的大文件，自动优化内存和性能
- **增强错误处理**：详细的错误信息和诊断输出

## 系统要求

- **操作系统**：Linux
- **依赖软件**：
  - Python 3
  - Ghostscript（大多数 Linux 发行版默认已安装）
- **硬件要求**：
  - 内存：建议至少 4GB RAM（处理大文件时需要更多）
  - 磁盘空间：至少为原始文件大小的 1.5 倍

## 安装方法

### 1. 检查并安装依赖

首先，确保系统已安装 Ghostscript：

```bash
# 检查 Ghostscript 是否已安装
which gs

# 如果未安装，使用以下命令安装
# Debian/Ubuntu
sudo apt install ghostscript

# CentOS/RHEL
sudo yum install ghostscript

# Fedora
sudo dnf install ghostscript
```

### 2. 下载脚本

将 `pdf_compress.py` 脚本下载到您的工作目录。

### 3. 设置执行权限

```bash
chmod +x pdf_compress.py
```

## 使用方法

### 基本语法

```bash
./pdf_compress.py [选项] 输入文件
```

### 可用选项

| 选项 | 描述 | 默认值 |
|------|------|--------|
| `-h, --help` | 显示帮助信息 | - |
| `-o, --output` | 指定输出文件路径 | 自动在输入文件名后添加 "_compressed" |
| `-q, --quality` | 指定压缩质量级别 | medium |

### 压缩质量级别

| 级别 | 描述 | 分辨率 | 适用场景 |
|------|------|--------|----------|
| `low` | 最低质量，最大压缩 | 72 DPI | 网络传输、快速预览、大文件压缩 |
| `medium` | 中等质量，平衡压缩 | 150 DPI | 一般用途、电子邮件附件 |
| `high` | 高质量，最小压缩 | 300 DPI | 打印、高质量输出 |

## 使用示例

### 示例 1：默认压缩（中等质量）

```bash
./pdf_compress.py document.pdf
```

输出文件将自动命名为 `document_compressed.pdf`。

### 示例 2：指定输出路径

```bash
./pdf_compress.py report.pdf -o report_small.pdf
```

### 示例 3：使用低质量压缩（最大压缩）

```bash
./pdf_compress.py presentation.pdf -q low
```

### 示例 4：使用高质量压缩（最小压缩）

```bash
./pdf_compress.py manual.pdf -q high -o manual_compressed.pdf
```

### 示例 5：压缩大文件（推荐 low 质量）

```bash
./pdf_compress.py large_document.pdf -q low -o compressed.pdf
```

## 输出说明

执行脚本后，您将看到类似以下的输出：

```
正在压缩 PDF 文件...
输入: document.pdf
输出: document_compressed.pdf
质量设置: medium (ebook, 150 DPI)
文件大小: 15.50 MB

压缩完成!
原始大小: 15.50 MB
压缩后大小: 5.20 MB
减少了: 66.45%
```

对于大文件（超过 100MB），还会显示提示信息：

```
提示: 处理大文件可能需要较长时间，请耐心等待...
```

## 大文件处理指南

### 处理时间估算

| 文件大小 | 文本密集型 | 图像密集型 |
|----------|-----------|-----------|
| 100MB | 1-3 分钟 | 3-8 分钟 |
| 300MB | 3-8 分钟 | 8-15 分钟 |
| 500MB | 5-12 分钟 | 12-25 分钟 |

*注：实际时间取决于硬件配置和 PDF 内容*

### 大文件优化建议

1. **选择合适的质量级别**
   - 对于大文件，建议使用 `low` 质量级别
   - 这样可以显著减少处理时间和内存使用

2. **确保足够的系统资源**
   - 内存：至少 4GB，推荐 8GB 以上
   - 磁盘空间：确保有原始文件 1.5 倍以上的可用空间
   - CPU：多核处理器可以加快处理速度

3. **处理过程中的注意事项**
   - 避免在处理过程中运行其他高内存占用的程序
   - 保持终端会话活跃，避免超时断开
   - 对于超大文件，考虑分割处理

## 常见问题

### 1. 脚本执行失败，提示找不到 Ghostscript

确保已正确安装 Ghostscript，并且 `gs` 命令在系统路径中。

### 2. 压缩后的文件质量不理想

尝试使用更高的质量级别，例如：

```bash
./pdf_compress.py input.pdf -q high
```

### 3. 压缩效果不明显

如果 PDF 文件已经过压缩，或者主要包含文本而不是图像，压缩效果可能不明显。

### 4. 处理大文件时出错或崩溃

**可能原因：**
- 内存不足
- 磁盘空间不足
- Ghostscript 参数限制

**解决方案：**
- 使用 `low` 质量级别减少内存使用
- 检查系统内存和磁盘空间
- 关闭其他占用内存的程序
- 尝试分批处理（将大文件拆分为多个小文件）

### 5. 压缩过程被中断或超时

**可能原因：**
- SSH 会话超时
- 终端被关闭
- 系统资源不足

**解决方案：**
- 使用 `nohup` 或 `screen` 在后台运行
- 增加系统超时设置
- 使用更快的质量级别

```bash
# 使用 nohup 在后台运行
nohup ./pdf_compress.py large.pdf -q low &

# 使用 screen 会话
screen -S pdfcompress
./pdf_compress.py large.pdf -q low
# 按 Ctrl+A, D 分离会话
```

### 6. 权限错误

确保脚本有执行权限，且对输入/输出目录有读写权限：

```bash
chmod +x pdf_compress.py
chmod 755 /path/to/output/directory
```

## 高级用法

### 批量压缩多个 PDF 文件

您可以使用 shell 脚本批量处理多个 PDF 文件：

```bash
for file in *.pdf; do
  ./pdf_compress.py "$file"
done
```

### 集成到其他工作流程

您可以将此脚本集成到文档处理工作流程中，例如在生成 PDF 后自动进行压缩：

```bash
# 生成 PDF 后自动压缩
pandoc document.md -o document.pdf && ./pdf_compress.py document.pdf
```

### 后台处理大文件

对于大文件，建议在后台运行以避免会话超时：

```bash
# 方法 1：使用 nohup
nohup ./pdf_compress.py large.pdf -q low > compress.log 2>&1 &

# 方法 2：使用 screen
screen -dmS pdfcompress ./pdf_compress.py large.pdf -q low

# 方法 3：使用 tmux
tmux new-session -d -s pdfcompress './pdf_compress.py large.pdf -q low'
```

### 监控处理进度

对于大文件，可以通过日志文件监控进度：

```bash
# 实时查看日志
tail -f compress.log

# 检查进程状态
ps aux | grep pdf_compress
```

## 技术细节

### Ghostscript 参数说明

脚本使用了以下 Ghostscript 参数来优化大文件处理：

| 参数 | 说明 | 值 |
|------|------|-----|
| `-dBufferSpace` | 缓冲区大小 | 64MB |
| `-dMaxBitmap` | 最大位图大小 | 500MB |
| `-dUseFastColor` | 快速颜色处理 | true |
| `-dNumRenderingThreads` | 渲染线程数 | 4 |

这些参数可以根据您的系统配置进行调整。

### 性能优化建议

1. **调整线程数**：根据 CPU 核心数调整 `-dNumRenderingThreads`
2. **增加缓冲区**：如果内存充足，可以增大 `-dBufferSpace`
3. **选择合适的质量级别**：平衡压缩率和处理时间

## 注意事项

- 压缩过程可能会降低 PDF 文件的质量，特别是使用低质量设置时
- 对于包含重要图像或图形的 PDF，建议使用高质量设置
- 压缩后的文件可能与某些 PDF 查看器或编辑器存在兼容性问题
- 始终保留原始 PDF 文件的备份，以防压缩后的文件不符合您的要求
- 处理大文件时，请确保有足够的系统资源和稳定的运行环境
- 建议在处理重要文件前先进行测试

## 故障排除

如果遇到问题，请检查以下几点：

1. **Ghostscript 版本**：确保版本较新（建议 9.50+）
   ```bash
   gs --version
   ```

2. **系统资源**：检查内存和磁盘空间
   ```bash
   free -h
   df -h
   ```

3. **文件权限**：确保有读写权限
   ```bash
   ls -la input.pdf
   ls -la /path/to/output/
   ```

4. **查看详细错误**：运行脚本时观察完整的错误输出

5. **测试小文件**：先用小文件测试，确认脚本正常工作

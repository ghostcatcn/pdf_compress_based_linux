#!/usr/bin/env python3
import os
import sys
import argparse

def compress_pdf(input_path, output_path, quality):
    """使用 Ghostscript 压缩 PDF 文件"""
    # 验证输入文件是否存在
    if not os.path.exists(input_path):
        print(f"错误: 输入文件 '{input_path}' 不存在")
        return False
    
    # 验证输入文件是否为 PDF
    if not input_path.lower().endswith('.pdf'):
        print("错误: 输入文件必须是 PDF 文件")
        return False
    
    # 如果未指定输出路径，在输入文件名后添加 "_compressed"
    if not output_path:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}_compressed.pdf"
    
    # 根据质量级别设置 Ghostscript 参数
    if quality == 'low':
        # 最低质量，最大压缩
        dpi = 72
        compression = 'screen'
    elif quality == 'medium':
        # 中等质量，中等压缩
        dpi = 150
        compression = 'ebook'
    elif quality == 'high':
        # 高质量，最小压缩
        dpi = 300
        compression = 'printer'
    else:
        # 默认中等质量
        dpi = 150
        compression = 'ebook'
    
    # 构建 Ghostscript 命令，添加大文件处理参数
    gs_command = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        f'-dPDFSETTINGS=/{compression}',
        f'-dNOPAUSE',
        f'-dQUIET',
        f'-dBATCH',
        f'-dPrinted=false',
        f'-r{dpi}',
        # 大文件处理优化参数
        '-dBufferSpace=67108864',  # 增加缓冲区大小（64MB）
        '-dMaxBitmap=500000000',   # 增加最大位图大小
        '-dUseFastColor=true',      # 使用快速颜色处理
        '-dNumRenderingThreads=4',  # 使用多线程渲染（根据CPU核心数调整）
        f'-sOutputFile={output_path}',
        input_path
    ]
    
    # 执行命令
    try:
        input_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
        print(f"正在压缩 PDF 文件...")
        print(f"输入: {input_path}")
        print(f"输出: {output_path}")
        print(f"质量设置: {quality} ({compression}, {dpi} DPI)")
        print(f"文件大小: {input_size:.2f} MB")
        
        # 对于大文件，给出处理时间提示
        if input_size > 100:
            print(f"提示: 处理大文件可能需要较长时间，请耐心等待...")
        
        # 执行命令并捕获返回值
        import subprocess
        result = subprocess.run(' '.join(gs_command), shell=True, capture_output=True, text=True)
        
        # 检查命令执行状态
        if result.returncode != 0:
            print(f"错误: Ghostscript 执行失败")
            print(f"错误输出: {result.stderr}")
            return False
        
        # 检查输出文件是否生成
        if os.path.exists(output_path):
            output_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
            reduction = ((input_size - output_size) / input_size) * 100
            
            print(f"\n压缩完成!")
            print(f"原始大小: {input_size:.2f} MB")
            print(f"压缩后大小: {output_size:.2f} MB")
            print(f"减少了: {reduction:.2f}%")
            return True
        else:
            print("错误: 压缩过程失败，未生成输出文件")
            return False
    except Exception as e:
        print(f"错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    parser = argparse.ArgumentParser(description='PDF 压缩工具')
    parser.add_argument('input', help='输入 PDF 文件路径')
    parser.add_argument('-o', '--output', help='输出 PDF 文件路径', default='')
    parser.add_argument('-q', '--quality', choices=['low', 'medium', 'high'], default='medium',
                        help='压缩质量级别 (默认: medium)')
    
    args = parser.parse_args()
    
    compress_pdf(args.input, args.output, args.quality)

if __name__ == '__main__':
    main()

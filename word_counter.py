"""
词频统计工具
读取一个文本文件，统计每个单词出现的频率，按出现次数从高到低排序输出。

用法：
    python word_counter.py <文件路径>          # 显示全部结果
    python word_counter.py <文件路径> --top N  # 只显示前 N 个
"""

import argparse
import sys
import re
from collections import Counter


def read_file(file_path):
    """读取文件内容并返回字符串"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 未找到")
        sys.exit(1)
    except Exception as e:
        print(f"错误：读取文件时发生异常 - {e}")
        sys.exit(1)


def count_words(text):
    """
    统计文本中的词频
    返回 (word, count) 列表，按出现次数降序排列
    """
    # 转换为小写，提取所有单词（只包含字母）
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return Counter(words).most_common()


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="词频统计工具")
    parser.add_argument("file", help="要分析的文件路径")
    parser.add_argument("--top", "-n", type=int, help="只显示出现次数最多的前 N 个词")
    return parser.parse_args()


def main():
    args = parse_args()

    text = read_file(args.file)
    word_counts = count_words(text)

    if not word_counts:
        print("文件中没有找到任何单词。")
        return

    # 如果指定了 --top，只取前 N 个
    if args.top and args.top > 0:
        word_counts = word_counts[:args.top]
        print(f"\n（仅显示前 {args.top} 个）")

    # 输出结果
    print(f"\n{'单词':<20} 出现次数")
    print("-" * 30)
    for word, count in word_counts:
        print(f"{word:<20} {count}")

    print(f"\n总计：{args.top if args.top else len(word_counts)} 个不同的单词")


if __name__ == "__main__":
    main()

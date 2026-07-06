"""
词频统计工具
读取一个文本文件，统计每个单词出现的频率，按出现次数从高到低排序输出。
"""

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


def main():
    if len(sys.argv) != 2:
        print("用法：python word_counter.py <文件路径>")
        print("示例：python word_counter.py sample.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    word_counts = count_words(text)

    if not word_counts:
        print("文件中没有找到任何单词。")
        return

    # 输出结果
    print(f"\n{'单词':<20} 出现次数")
    print("-" * 30)
    for word, count in word_counts:
        print(f"{word:<20} {count}")

    print(f"\n总计：{len(word_counts)} 个不同的单词")


if __name__ == "__main__":
    main()

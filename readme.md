# Word count

ccwc is a custom command-line utility inspired by the classic wc command. This versatile tool allows you to count words, bytes, characters, and lines in a file or text stream with ease. Whether you need to analyze text files or input from stdin, ccwc is here to provide you with essential counting options. It's designed for simplicity, making it a valuable addition to your command-line toolkit.

## Motivation

[John Crickett coding challenege 1](https://codingchallenges.fyi/challenges/challenge-wc)

## Options supported

```
-w: Display word count.
-c: Display byte count.
-m: Display character count.
-l: Display line count.
```

## Requirements

- Python3.x

## How to run

```bash
> python3 ccwc.py -w text.txt
Word count : 58164

> python3 ccwc.py -l -c text.txt
Line count : 7145
Byte count : 342190
```

input from pipe is also supported

```bash
> cat test.txt | python3 ccwc.py
Line count : 7145
Byte count : 342190
Word count : 58164
```

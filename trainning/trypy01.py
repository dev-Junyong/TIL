
# 1번
def make_comma(n):
    n = str(n)
    if n[0] == '-':
        return '-' + make_comma(n[1:])
    if len(n) <= 3:
        return n
    if n.find('.') == -1:
        return make_comma(n[:-3]) + ',' + n[-3:]
    else:
        return make_comma(n[:n.find('.')]) + n[n.find('.'):]

print(make_comma(1000000))

# 2번
# 파일 저장이나 열기는 익숙치 않아서 예시코드 참고했습니다.
def count_word(text, word):
    text_save = open("text.txt", "w", encoding="UTF8")
    text_save.write(text)
    text_save.close()

    cnt = 0
    length = len(word)
    new_word = ""

    f_1 = open("text.txt")
    for line in f_1:
        if word in line: 
            for s in line:
                new_word += s
                if new_word == word:
                    cnt += 1
                if len(new_word) == length:
                    new_word = new_word[1:]
    return cnt

a = "안녕하세요. 반갑습니다. 파이썬 공부는 정말 재밌습니다."
print(count_word(a, "습니다"))




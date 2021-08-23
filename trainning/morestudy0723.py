#관통 프로젝트, 교수님 코드 따라하기
#1.
import json
from pprint import pprint


def movie_info(movie):
    # pprint(movie)
    # 여기에 코드를 작성합니다.    
    # print(movie['title'])
    detail = {
        'id': movie['id'],
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average': movie['vote_average'],
        'overview': movie['overview'],
        'genre_ids': movie['genre_ids'],
    }
    return detail

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


#2.




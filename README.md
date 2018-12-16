## CRUD Board Functions
* 회원가입이 가능합니다.
* 로그인 후 포스트 목록을 볼 수 있습니다.
* 최신순으로 정렬된 포스트와 내가 작성한 포스트의 목록을 확인할 수 있습니다.
* 포스트를 클릭하여 내용을 확인할 수 있습니다.
* main/이전/다음으로 이동할 수 있습니다.
* 내가 작성한 포스트의 경우에만 편집/삭제할 수 있습니다.

## Preview
![capture](/assets/capture.png)
![capture](/assets/capture2.png)
![capture](/assets/capture3.png)
![capture](/assets/capture4.png)
![capture](/assets/capture5.png)
![capture](/assets/capture6.png)
![capture](/assets/capture7.png)

## Start project
```bash
$ cd waffle_hw2
$ pip install -r requirements.txt
$ python manage.py makemigrations board member
$ python manage.py migrate
$ python manage.py runserver
```

## References
* [django girls](https://tutorial.djangogirls.org/ko/django_start_project/)
* [waffle seminar](https://waffle-skile.github.io/lecture/3/)
* [django official documentation](https://docs.djangoproject.com/ko/2.1/topics/auth/default/)
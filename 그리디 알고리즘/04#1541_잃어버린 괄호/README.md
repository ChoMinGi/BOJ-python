생각을 해본다면 첫번째로 받아오는 값(+를 통해 얻어지는 값 포함)은 - 가 나오기 전까지는 덧셈을 하는 수밖에 없다.

예로 들어서 5+5+5-5 라는 식이 존재한다고 가정했을때 괄호를 아무리 배치해도 결과값은 15-5로 나오게 된다.

따라서 값을 먼저 -로 split 을 한 후에 나머지 값들(단일값, +로 이루어진 수식) 을 계산을 한 후에 전부 처음값에서 빼주면 된다.

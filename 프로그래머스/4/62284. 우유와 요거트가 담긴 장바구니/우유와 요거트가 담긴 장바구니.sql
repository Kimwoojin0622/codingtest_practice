# 우유와 요거트가 담긴 장바구니

# 테이블 1 - CART_PRODUCTS 테이블
  # 아이디, 장바구니의 아이디, 상품 종류, 가격
  
# 문제 : 우유 Milk와 요거트 Yogurt를 동시에 구입한 장바구니의 아이디를 조회하는 SQL문을 작성
# 장바구니의 아이디 순으로 출력

# 1. CART_PRODUCTS 테이블에서 Milk와 Yogurt만 구매한 장바구니를 원했기 때문에, NAME 컬럼을 활용하여 WHERE절에서 IN 연산자를 통해 Milk와 Yogurt만 있는 행을 출력

# 2. 이후 CART_ID를 기준으로 GROUP BY를 진행하고, HAVING 절을 통해 Milk와 Yogurt를 동시에 담은 사람들을 찾기 위해 NAME 컬럼을 COUNT() 집계의 값이 = 2인 CART_ID가 존재하는지 출력

# 3. 이 과정에서 한 사람이 Yogurt는 구매하지 않았지만, milk만 여러 개 구매했을 때, Milk만 구매한 사람의 COUNT(NAME) 값이 2개 이상이 나올 수 있기 때문에, DISTINCT를 활용하여 NAME의 중복을 제거함으로써, milk와 yogurt를 구매한 사람들만 COUNT() 집계 함수 값이 2가 되게끔 만들었습니다.

# 4. 마지막으로는 CART_ID를 기준으로 오름차순을 진행했습니다.

SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt')
GROUP BY CART_ID
  HAVING COUNT(DISTINCT NAME) = 2
ORDER BY CART_ID ASC;
# USED_GOODS_BOARD 테이블 - 중고 거래 게시판 정보를 담은 테이블
# USED_GOODS_USER 테이블 - 게시판 사용자 정보를 담은 테이블

# 완료된 중고 거래의 총 금액이 70만원 이상인 사람의 회원 ID, 닉네임, 총 거래 금액!
SELECT UGU.USER_ID
     , UGU.NICKNAME
     , SUM(UGB.PRICE) AS 'TOTAL_SALES'
FROM USED_GOODS_BOARD AS UGB
  # 최종 값은 USED_GOODS_USER에 있는 회원 ID, 닉네임, 총 거래 금액을 원하기 때문에,
  # USED_GOODS_USER와 JOIN을 진행 (공통 컬럼 UGB의 WRITER_ID와 UGU의 USER_ID으로 조인)
  INNER JOIN USED_GOODS_USER AS UGU ON UGB.WRITER_ID = UGU.USER_ID
# 완료된 중고 거래의 데이터를 원하기 때문에 USED_GOODS_BOARD 테이블에서 STATUS가 DONE인 행을 선택
WHERE UGB.STATUS = 'DONE'
# 또한 그 값이 70만원을 넘어야 되기 때문에 USER_ID를 GROUP BY 하여 HAVING절을 통해 70만원 이상인 사람만 추출
GROUP BY UGU.USER_ID
  HAVING SUM(UGB.PRICE) >= 700000
# 마지막으로, 결과는 총거래금액을 기준으로 오름차순으로 정렬을 해야함
ORDER BY SUM(UGB.PRICE) ASC;
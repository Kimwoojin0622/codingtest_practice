# 취소되지 않은 진료 예약 조회하기

# 테이블1 -> 환자 정보를 담은 PATIENT 테이블 / 환자번호, 환자이름, 성별코드, 나이, 전화번호 컬럼 존재
# 테이블2 -> 의사 정보를 담은 DOTOR 테이블 / 의사이름, 의사ID, 면허번호, 진료과코드 등이 존재
# 테이블3 -> 진료 예약 정보를 담은 APPOINTMENT 테이블 / 진료 예약 일시, 진료 예약 번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소날짜 등이 존재

# 문제 -> 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성
# 결과는 진료예약일시를 기준으로 오름차순 정렬

# 1. APPOINTMENT 테이블을 통해 WHERE절에서 진료예약일시가 2022년 4월 13일인 데이터를 DATE_FORMAT 함수를 활용해서 출력했습니다.
# 2. 또한 취소가 되지 않으면서, 흉부외과를 원했기 때문에 APPOINTMENT 테이블의 APNT_CNCL_YN 컬럼 값이 N인 것과 MCDP_CD가 CS인 것을 AND를 통해 조건을 걸었습니다.
# 3. 최종 출력에는 환자 이름과 의사 이름도 요구하고 있기 때문에, APPOINTMENT의 PT_NO 컬럼과 PATIENT 테이블의 PT_NO, APPOINTMENT의 MDDR_ID 컬럼과 DORTOR 테이블의 DR_ID 컬럼을 JOIN했습니다.
# 4. 이를 통해 최종 출력에서 SELECT문을 통해 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 표시되게끔 진행했습니다.
# 5. 마지막으로 진료예약일시를 기준으로 오름차순을 진행하기 위해 ORDER BY 문에 APNT_YMD 컬럼에 오름차순을 진행했습니다.

SELECT A.APNT_NO
     , P.PT_NAME
     , A.PT_NO
     , A.MCDP_CD
     , D.DR_NAME
     , A.APNT_YMD
FROM APPOINTMENT AS A
  INNER JOIN PATIENT AS P ON A.PT_NO = P.PT_NO
  INNER JOIN DOCTOR AS D ON A.MDDR_ID = D.DR_ID
WHERE DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
  AND A.APNT_CNCL_YN = 'N'
  AND A.MCDP_CD = 'CS'
ORDER BY A.APNT_YMD ASC;
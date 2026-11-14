# ANIMAL_INS는 동물보호소에 들어온 동물의 정보 (동물의 아이디, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부 등)
# ANIMAL_OUTS는 동물보호소에서 입양 보낸 동물의 정보 (동물의 아이디, 입양일, 이름, 성별 및 중성화 여부)

# 보호소에서 중성화 수술을 거친 동물의 정보를 알아보려고 함!
# 보호소에 들어올 당시 ANIMAL_INS에서는 중성화가 되어 있지 않았지만, 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회
# ** 중성화를 거친 동물은 Spayed 또는 Neutered라고 표시되어 있음

# 1. 보호소에 있다가 입양을 간 데이터를 기준으로 하기 때문에, ANIMAL_INS와 ANIMAL_OUTS의 ANIMAL_ID 컬럼을 기준으로 JOIN을 진행하였다.
# 2. 조건절 에서 들어 왔을 당시, ANIMAL_INS의 INTAKE는 Intact이고
# 보호소에서 나갈 딩시, ANMIAL_OUTS의 INTAKE가 Spayed 또는 Neutered인 행을 찾는다.
SELECT AI.ANIMAL_ID
     , AI.ANIMAL_TYPE
     , AI.NAME
FROM ANIMAL_INS AS AI
  INNER JOIN ANIMAL_OUTS AS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
 # AI의 INTAKE의 값에서 Intact가 있는 행을 찾기 위해 LIKE 연산자 활용
WHERE AI.SEX_UPON_INTAKE LIKE '%Intact%'
AND (AO.SEX_UPON_OUTCOME LIKE '%Spayed%' OR AO.SEX_UPON_OUTCOME LIKE '%Neutered%') 
# 마지막에 아이디 순으로 조회
ORDER BY AI.ANIMAL_ID ASC;

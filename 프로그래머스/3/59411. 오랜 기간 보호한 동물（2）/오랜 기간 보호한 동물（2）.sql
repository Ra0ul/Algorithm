-- 코드를 입력하세요
SELECT ANIMAL_ID, i.NAME FROM ANIMAL_INS i
INNER JOIN ANIMAL_OUTS o
USING (ANIMAL_ID)
ORDER BY DATEDIFF(o.DATETIME,i.DATETIME) DESC
LIMIT 2
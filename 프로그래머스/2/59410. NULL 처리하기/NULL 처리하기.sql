-- 코드를 입력하세요
SELECT 
    ANIMAL_TYPE,
    -- if(NAME is null, 'No name', NAME) NAME,
    coalesce(NAME, 'No name') NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS

ORDER BY ANIMAL_ID
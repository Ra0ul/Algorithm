
-- 년, 월 별로 출력
SELECT COUNT(*) INTO @TOTAL FROM USER_INFO
            WHERE joined LIKE '2021%';

SELECT 
    year(sales_date) YEAR, 
    month(sales_date) MONTH, 
    count(DISTINCT USER_ID) PUCHASED_USERS, -- 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수
    round(count(DISTINCT USER_ID)/@TOTAL,1) PUCHASED_RATIO -- 2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수
FROM ONLINE_SALE

INNER JOIN (SELECT * FROM USER_INFO
            WHERE joined LIKE '2021%') i
USING(USER_ID)
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH
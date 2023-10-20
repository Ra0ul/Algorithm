-- 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 
-- 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 
-- 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.
SELECT USER_ID, u.NICKNAME, sum(PRICE) TOTAL_SALEs FROM USED_GOODS_BOARD b 
INNER JOIN USED_GOODS_USER u 
ON b.WRITER_ID = u.USER_ID

where STATUS LIKE 'DONE' 
 -- WHERE STATUS LIKE 'DONE' 
-- AND sum(PRICE)>700000
group by USER_ID 
having sum(PRICE)>=700000 
-- having STATUS LIKE 'DONE' AND sum(PRICE)>700000) new
order by TOTAL_SALEs
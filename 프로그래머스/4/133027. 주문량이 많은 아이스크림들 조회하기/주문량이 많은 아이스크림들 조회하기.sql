-- 그냥 inner join으로 해결 가능~~ 그럼 조인 테이블에서 가져올 수있음

SELECT FLAVOR FROM FIRST_HALF f
LEFT JOIN
(SELECT FLAVOR, sum(TOTAL_ORDER) JULY_TOTAL FROM JULY
GROUP BY FLAVOR) j
USING (FLAVOR)
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER+JULY_TOTAL) DESC
LIMIT 3
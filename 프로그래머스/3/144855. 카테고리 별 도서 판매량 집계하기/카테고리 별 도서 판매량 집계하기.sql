-- 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요.

-- 결과는 카테고리명을 기준으로 오름차순 정렬
-- select CATEGORY, price*total TOTAL_SALES from
SELECT CATEGORY, sum(SALES) TOTAL_SALES from BOOK b 
inner join BOOK_SALES s -- 여기서 두 테이블을 책 Id기준으로 함쳤고
using (BOOK_ID)
where SALES_DATE like "2022-01%"
group by CATEGORY
-- having SALES_DATE like "2022-01%" 평균 합산 등의 통계치에 사용하는 having
order by CATEGORY 
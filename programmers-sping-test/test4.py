'''
sql
employees 테이블,
id, name, salary, branch_id

아이디, 이름, 월급, 근무하는 대리점

각 대리점에서 월급이 제일 많은 사람 가져오기
'''
'''
select EMPLOYEES.BRANCH_ID, EMPLOYEES.NAME from EMPLOYEES, (
    SELECT BRANCH_ID, max(SALARY) as SALARY FROM EMPLOYEES   Group By BRANCH_ID
) t1 where EMPLOYEES.BRANCH_ID = t1.BRANCH_ID and EMPLOYEES.SALARY = t1.SALARY ORDER BY BRANCH_ID,  name ASC
'''

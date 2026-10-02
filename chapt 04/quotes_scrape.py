import pandas as pd
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 초기 설정
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # 웹페이지 오픈
    driver.get('https://quotes.toscrape.com/')
    # 웹페이지 다 오픈될때까지 대기
    footer = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'footer'))
    )
    # 로그인 링크 가져오기
    login_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))
    )
    login_link.click()

    # 로그인 
    # 아이디 패스워드 입력
    username_input = wait.until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    password_input = driver.find_element(By.ID, 'password')

    username_input.send_keys('admin')
    password_input.send_keys('admin')

    # 로그인버튼 클릭
    login_btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    login_btn.click()

    # 로그인 완료확인 대기
    wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))        
    )
    print('로그인 성공')

    # 100건 - 10페이지 반복
    rows = []

    # 페이지번호 
    for page_num in range(1, 11):
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'footer'))
        )

        print(f'{page_num} 페이지 수집')
        
        quotes = driver.find_elements(By.CSS_SELECTOR, '.quote')

        for qoute in quotes: # 한 페이지당 10개를 하나씩 반복
            text = qoute.find_element(By.CSS_SELECTOR, '.text').text
            author = qoute.find_element(By.CSS_SELECTOR, '.author').text
            link = qoute.find_elements(By.CSS_SELECTOR, 'span > a')[1].get_attribute('href')
            tags = qoute.find_elements(By.CSS_SELECTOR, '.tags > a')
            tag_text = ', '.join(tag.text for tag in tags)

            rows.append({
                'text': text,
                'author': author,
                'link': link,
                'tags': tag_text
            })

        if page_num == 10:
            break

        # 다음 페이지가 없으면 빈 리스트를 반환
        next_button = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
        if not next_button:
            break
        previous_quote = quotes[0]
        next_button[0].click()
        wait.until(EC.staleness_of(previous_quote))

    if len(rows) != 100:
        raise ValueError(f'100개 수집 필요: 현재 {len(rows)}개')
    df_quotes = pd.DataFrame(rows)
    # 저장
    output_path = Path(__file__).resolve().parent.parent / 'data' / 'quotes_to_scrap_100.csv'
    df_quotes.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f'100개 데이터 저장 완료: {output_path}')

    # 로그아웃
    logout_link = driver.find_element(By.LINK_TEXT, 'Logout')
    logout_link.click()
    print('로그아웃 완료')
except Exception as error:
    print('실행 중 오류 발생', error)
    raise
finally:
    # 브라우저 종료
    driver.quit()

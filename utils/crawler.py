import requests
from bs4 import BeautifulSoup
import time
import os
from typing import Dict, Any
from utils.logger import setup_logger, log_problem_data
from utils.config import DEFAULT_CONFIG

def crawl_acmicpc_problem(problem_id: str, save_to_json: bool = True) -> Dict[str, Any]:
    logger = setup_logger(DEFAULT_CONFIG["debug_mode"])
    url = f"{DEFAULT_CONFIG['acmicpc_url']}{problem_id}"
    headers = {"User-Agent": DEFAULT_CONFIG["user_agent"]}
    html_file = f"logs/acmicpc_{problem_id}.html"

    logger.info(f"Extracted problem ID: {problem_id}")
    try:
        # HTML 파일 존재 여부 확인
        if os.path.exists(html_file):
            logger.info(f"Using cached HTML file for problem {problem_id}: {html_file}")
            with open(html_file, "r", encoding="utf-8") as f:
                html_content = f.read()
        else:
            logger.info(f"Starting crawl for problem {problem_id}")
            response = requests.get(url, headers=headers)

            # Response 디버깅 정보 (디버그 모드)
            if DEFAULT_CONFIG["debug_mode"]:
                logger.debug(f"Response Status Code: {response.status_code}")
                logger.debug(f"Response URL: {response.url}")
                logger.debug(f"Response Headers: {response.headers}")
                logger.debug(f"Response Encoding: {response.encoding}")
                logger.debug(f"Response Text (first 200 chars): {response.text[:200]}...")

            response.raise_for_status()
            html_content = response.text

            # HTML 파일 저장
            os.makedirs("logs", exist_ok=True)
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)
                logger.info(f"Saved HTML for problem {problem_id} to {html_file}")

        # HTML 파싱 id/class가 바뀔 수 있음
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find('title').text.strip()
        description = soup.find('div', id='problem_description').text.strip()
        problem_input = soup.find('div', id='problem_input').find_next('p').text.strip() if soup.find('div', id='problem_input') else ""
        problem_output = soup.find('div', id='problem_output').find_next('p').text.strip() if soup.find('div', id='problem_output') else ""
       
        # 샘플 데이터 추출
        sample_data = {}
        sample_inputs = soup.find_all('pre', class_='sampledata', id=lambda x: x and x.startswith('sample-input-'))
        sample_outputs = soup.find_all('pre', class_='sampledata', id=lambda x: x and x.startswith('sample-output-'))
        
        for i, sample_input in enumerate(sample_inputs, 1):
            sample_data[f"input_{i}"] = sample_input.text.strip()
        for i, sample_output in enumerate(sample_outputs, 1):
            sample_data[f"output_{i}"] = sample_output.text.strip()

        data = {
            "problem_id": problem_id,
            "title": title,
            "description": description,
            "problem_input": problem_input,
            "problem_output": problem_output,
            "sample_data": sample_data
        }

        # 로그 기록
        log_problem_data(problem_id, data)

        # JSON 저장
        # if save_to_json:
        #     os.makedirs("shared", exist_ok=True)
        #     with open(f"shared/{problem_id}.json", "w", encoding="utf-8") as f:
        #         json.dump(data, f, ensure_ascii=False, indent=2)
        #         logger.info(f"Saved problem {problem_id} data to shared/{problem_id}.json")

        return data
        
    except requests.RequestException as e:
        logger.error(f"Request failed for problem {problem_id}: {e}")
        return {}
    except AttributeError as e:
        logger.error(f"Parsing error for problem {problem_id}: {e}")
        return {}
    except IOError as e:
        logger.error(f"File I/O error for problem {problem_id}: {e}")
        return {}
    finally:
        if 'response' in locals():
            time.sleep(1)  # 크롤링 시에만 속도 제한
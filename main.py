import sys
import os
import importlib
import inspect
import re
from datetime import datetime
from utils import crawl_acmicpc_problem, setup_logger, DEFAULT_CONFIG

# sys.path 설정
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# 로거 설정
logger = setup_logger(DEFAULT_CONFIG["debug_mode"])

# 파일 이름 입력
file_name = input("FILE NAME (ex: 250901, Just enter if you want today): ").strip()

try:
    if not file_name:
        file_name = datetime.now().strftime("%y%m%d")
        logger.info(f"Activating today's file: {file_name}")

    # 동적 임포트
    module = importlib.import_module(f"problems.{file_name}")
    logger.debug(f"Imported module: problems.{file_name}")

    # 함수 목록 가져오기
    functions = [name for name, obj in inspect.getmembers(module, inspect.isfunction)]
    if not functions:
        logger.error(f"No functions found in {file_name}.py")
        print(f"Err) NO functions in {file_name}.py")
        sys.exit(1)

    # 함수 목록 출력 및 선택
    logger.info(f"Functions in {file_name}: {', '.join(functions)}")
    print(f"\n[problems/{file_name}]")
    for i, func_name in enumerate(functions, 1):
        print(f"{i}. {func_name}")
    
    while True:
        choice = input(f">> Choose (1-{len(functions)}, Just enter for 1): ").strip()
        if not choice:
            func_name = functions[0]
            logger.info(f"Activating function: {func_name}")
            print(f"::: Activate example ::: {func_name} \n")
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(functions):
                func_name = functions[index]
                logger.info(f"Selected function: {func_name}")
                print(f"Selected function: {func_name}")
                break
            else:
                logger.warning(f"Invalid number entered: {choice}. Must be 1-{len(functions)}")
                print(f"Err) enter valid number!! (1-{len(functions)}).")
        except ValueError:
            logger.warning(f"Non-numeric input: {choice}")
            print(f"Err) enter only number!! (1-{len(functions)}).")

    # 문제 번호 추출
    problem_id = re.search(r'acmicpc(\d+)', func_name)
    if problem_id:
        problem_id = problem_id.group(1)
        # 크롤링 데이터 가져오기
        problem_data = crawl_acmicpc_problem(problem_id)

        if problem_data:
            print(f"\n[{problem_data['title']}]{problem_data['description']}\n")
            print(f"입력 형식: {problem_data['problem_input']}\n")
            print(f"출력 형식: {problem_data['problem_output']}\n")

            # 함수 실행
            func = getattr(module, func_name)
            if func and problem_data['sample_data']:
                result = func(problem_data['sample_data'])

        else:
            logger.error(f"No data retrieved for problem {problem_id}")
            print(f"Err) Failed to retrieve problem data for {problem_id}")

except ModuleNotFoundError:
    logger.error(f"No such file problems/{file_name}.py")
    print(f"Err) No such file problems/{file_name}.py!! check path: {os.path.abspath(os.path.dirname(__file__))}")
    sys.exit(1)
except Exception as e:
    logger.error(f"Error occurred: {e}")
    print(f"Err) {e}")
    if DEFAULT_CONFIG["debug_mode"]:
        import traceback
        traceback.print_exc()
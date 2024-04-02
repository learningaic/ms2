import Langchain
import os
import PyPDF2

##pip3 install langchain PyPDF2

# Langchain 프레임워크 초기화
lc = Langchain()

# PDF 파일 크롤링 및 자동 업로드 함수
def crawl_and_upload_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        # PDF 파일을 읽어와서 텍스트 추출
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extract_text()

        # 추출한 텍스트를 Langchain에 업로드
        document_id = lc.upload_text(text)

    return document_id

# PDF에서 단어 검색 함수
def search_word_in_pdf(document_id, search_word):
    # Langchain에서 특정 단어 검색
    results = lc.search(document_id, search_word)
    return results

# 예제 사용
if __name__ == "__main__":
    # PDF 파일 경로
    pdf_path = "./1023.pdf"

    # PDF 크롤링 및 업로드
    document_id = crawl_and_upload_pdf(pdf_path)

    # 검색할 단어
    search_word = "검색할_단어"

    # 단어 검색
    search_results = search_word_in_pdf(document_id, search_word)

    # 검색 결과 출력
    print(f"검색 결과: {search_results}")

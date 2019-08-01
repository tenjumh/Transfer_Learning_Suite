from google_images_download import google_images_download
import ssl, os, sys  # ssl Error 발생 시

ssl._create_default_https_context = ssl._create_unverified_context
args = sys.argv[1:]
for keyword in args:
    def imageCrawling(keyword):
        response = google_images_download.googleimagesdownload()
        path = './dataset/train/'
        os.mkdir(path + keyword)
        dir = path + keyword
        arguments = {"keywords": keyword,  # 검색 키워드
                     #"suffix_keywords": subkeyword, #메인 키워드 추가 키워드
                     "limit": 100,  # 크롤링 이미지 수
                     "format": "jpg",  #jpg, gif, png, bmp, svg, webp, ico
                     #"size": , #large, medium, icon, >400*300, >640*480, >800*600, >1024*768, >2MP, >4MP, >6MP, >8MP, >10MP
                     #"time": , #past-24-hours, past-7-days
                     "print_urls": True,  # 이미지 url 출력
                     "no_directory": True,  #
                     'output_directory': dir}  # 크롤링 이미지를 저장할 폴더

        paths = response.download(arguments)
    imageCrawling(keyword)
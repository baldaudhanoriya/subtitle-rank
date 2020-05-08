import sys
sys.path.append("D:\\Coding\\Python\\Python")
import exe_no
import subtitles_functions


temp, known_words, length, important, prefix, suffix, subtitle, rank = subtitles_functions.opener()

repeated=subtitles_functions.main(temp, known_words, length, prefix, suffix)

subtitles_functions.last(important, subtitle, rank, temp, repeated)

exe_no.database(__file__)       
input("waiting to close")
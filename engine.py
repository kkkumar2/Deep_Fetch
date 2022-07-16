from paddleocr import PaddleOCR
from YOLOX.tools.demo import data,main,inference
from paddleocr import PaddleOCR
import re


def load_model():
    ocr = PaddleOCR(use_angle_cls=True, lang='en') 
    args,exp = data()
    predictor,args = main(exp, args,"yolox_s.pth")
    return ocr,args,predictor


ocr,args,predictor = load_model()


def run(image_path):
    result = ocr.ocr(image_path, cls=True)
    inference(predictor,args,image_path)
    value ={}
    value.setdefault('name',0) 
    value.setdefault("gender",0)
    value.setdefault('DOB',0)
    value.setdefault("aadhar",0)

    for line in result:
        string = line[1][0]
        
        """ re.IGNORECASE or re.I is the lower all the letter"""
        if (not value['DOB']) & (not value['gender']) & (not value['aadhar']) :
            """ if once reach dob or gender or aadhar then there is no name so we don't need if any thing detected any string which look like name """
            if (not re.search(r'[0-9]+|male|:|india|government',string,flags=re.IGNORECASE))&(" " in string):
                """ if any string contains digit or gender or ':'(father:name) or india or government  and also this string contains first name and last name """
                value['name'] = string
        
        if (len(string.replace(" ",""))==12 ) & (all(char.isdigit() for char in string.replace(" ",""))):
            """ first remove space this stirng and string len should be 12 and all the string is digit """
            value['aadhar'] = " ".join([string.replace(" ","")[i:i+4] for i in range(0,12,4)])

        gender = re.search(r'female|male',string,flags=re.IGNORECASE)
        """ if any string female or male  extract that much string any search string
            there is also reason if first added female beacause if added male  first then search string every time detect male (fe'male') """
        if gender:
            value['gender'] = gender.group().lower()

        dob = re.search(r"\d{2}/\d{2}/\d{2,4}|birth",string,flags=re.IGNORECASE)
        """ search string 00/00/0000 or 0000 or birth"""
        if dob:
            if all(char.isalpha() for char in dob.group()):
                "if all the string digit and then added date of birth"
                value['DOB'] = re.search(r"\d{2}/\d{2}/\d{2,4}|\d+",string).group()
            else:
                value['DOB'] = dob.group()
        
    print(value)


if __name__ == "__main__":
    run("20220705_174920.jpg")

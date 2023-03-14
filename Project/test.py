from googletrans import Translator
import tqdm
translator = Translator()
chinese_text = "我是精神美国人，只抽电子烟，从不看战狼，不用华为只用苹果手机"
japanese_text="私はスピリチュアルなアメリカ人です。電子タバコしか吸わないし、Wolf Warriors も見ません。Huawei も使用せず、Apple の電話しか使用しません"
english_text = translator.translate(japanese_text, src='auto', dest='en').text
print(english_text)